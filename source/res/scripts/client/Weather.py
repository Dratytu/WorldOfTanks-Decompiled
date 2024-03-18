# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/Weather.py

import random
import traceback
from vehicle_systems.stricted_loading import makeCallbackWeak
import BigWorld
import ResMgr
from Listener import Listenable
import Math

# Check if the current component is 'editor' or 'game'
if BigWorld.component != 'editor':
    import game as Personality
else:
    import Personality

# Load weather configuration from XML file
weatherXML = ResMgr.openSection('scripts/weather.xml')

class WeatherSystem(object):
    """
    A class representing a weather system with various properties like skyBoxes,
    rain, sun, ambient, windSpeed, windGustiness, skyBoxFogFactor, and fog.
    """

    def __init__(self, ds):
        """
        Initialize the WeatherSystem object with data from the given data section (ds).
        """
        self.name = ds.name
        self.skyBoxes = list(ds.readStrings('skyBox'))
        self.skyBoxModels = []
        self.rain = ds.readFloat('rain', 0.0)
        self.sun = ds.readVector4('sun', (1, 1, 1, 1))
        self.ambient = ds.readVector4('ambient', (1, 1, 1, 1))
        self.fog = ds.readVector4('fog', (1, 1, 1, 1))
        self.windSpeed = ds.readVector2('windSpeed', (0.0, 0.0))
        self.windGustiness = ds.readFloat('windGustiness', 0.0)
        self.skyBoxFogFactor = ds.readFloat('fogFactor', 0.15)
        self.fader = Math.Vector4Morph()
        self.fader.duration = 1.0
        f = self._fogAmount(self.fog[3])
        self.fader.target = (f,
                             0,
                             1,
                             0)
        self.fxName = ds.readString('sfx')
        self.loaded = False

    def _loadSkyBoxes(self, callback=None, immediate=False):
        """
        Load skybox models asynchronously or synchronously based on the 'immediate' flag.
        """
        if self.loaded:
            if callback:
                callback()
        elif not immediate:
            BigWorld.loadResourceListBG(self.skyBoxes, makeCallbackWeak(self._onLoadSkyBoxes, callback))
        else:
            resourceRefs = {}
            for i in self.skyBoxes:
                try:
                    resourceRefs[i] = BigWorld.Model(i)
                except ValueError:
                    resourceRefs[i] = BigWorld.Model('')

            self._onLoadSkyBoxes(callback, resourceRefs)

    def _onLoadSkyBoxes(self, callback, resourceRef):
        """
        Callback function for loading skybox models.
        """
        self.loaded = True
        for sb in self.skyBoxes:
            try:
                self.skyBoxModels.append(resourceRef[sb])
            except ValueError:
                self.skyBoxModels.append(BigWorld.Model(''))

        if callback is not None:
            callback()
        return

    def _unload(self):
        """
        Unload skybox models and reset the weather system properties.
        """
        for i in self.skyBoxModels:
            BigWorld.delSkyBox(i, self.fader)

        self.skyBoxModels = []
        self.loaded = False

    def fadeIn(self, fadingIn, fadeSpeed, immediate=False):
        """
        Fade in or out the weather system based on the 'fadingIn' flag.
        """
        curr = self.fader.value
        if fadingIn:
            if not self.loaded:
                print "calling fadeIn on a weather system that isn't loaded. please call prepareResources() first",
                print self.name
                traceback.print_stack()
                return
            for sb in self.skyBoxModels:
                if sb is not None:
                    BigWorld.addSkyBox(sb, self.fader)

            f = self._fogAmount(self.fog[3])
            self.fader.duration = fadeSpeed - 0.1
            self.fader.target = (f,
                                 0,
                                 1,
                                 1)
            try:
                BigWorld.weather().windAverage(self.windSpeed[0], self.windSpeed[1])
                BigWorld.weather().windGustiness(self.windGustiness)
            except ValueError:
                pass
            except EnvironmentError:
                pass

        elif self.loaded:
            sfxFadeSpeed = self._fadeOutFX()
            if not immediate:
                fadeSpeed = max(fadeSpeed, sfxFadeSpeed)
            BigWorld.callback(fadeSpeed, self._unload)
            self.fader.duration = fadeSpeed - 0.1
            self.fader.target = (curr[0],
                                 curr[1],
                                 curr[2],
                                 0)
        return

    def _fogAmount(self, amount):
        """
        Calculate the fog amount based on the given 'amount'.
        """
        return (amount - 1.0) * self.skyBoxFogFactor

    def prepareResources(self, callback=None, immediate=False):
        """
        Prepare weather system resources by loading skyboxes.
        """
        if not self.loaded:
            self._loadSkyBoxes(makeCallbackWeak(self._loadFX, callback), immediate)
        elif callback:
            callback()

    def setFadeSpeed(self, duration):
        """
        Set the fade speed for the weather system.
        """
       
