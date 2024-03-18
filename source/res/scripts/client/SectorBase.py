# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/SectorBase.py

import BigWorld
import ResMgr
import SoundGroups
from helpers import dependency
from FlagModel import FlagSettings, FlagModel
from Math import Vector4, Vector3, Vector2, Matrix
from skeletons.account_helpers.settings_core import ISettingsCore
from account_helpers.settings_core.settings_constants import GRAPHICS
import AnimationSequence

# A class to cache sector base settings
class _SectorBaseSettingsCache(object):
    def __init__(self, settings):
        self.initSettings(settings)

    def initSettings(self, settings):
        self.flagModelName = settings.readString('flagModelName', '')
        self.flagStaffModelName = settings.readString('flagstaffModelName', '')
        self.radiusModel = settings.readString('radiusModel', '')
        self.flagAnim = settings.readString('flagAnim', '')
        self.flagStaffFlagHP = settings.readString('flagstaffFlagHP', '')
        self.baseAttachedSoundEventName = settings.readString('wwsound', '')
        self.flagBackgroundTex = settings.readString('flagBackgroundTex', '')
        self.flagEmblemTex = settings.readString('flagEmblemTex', '')
        self.flagEmblemTexCoords = settings.readVector4('flagEmblemTexCoords', Vector4())
        self.flagScale = settings.readVector3('flagScale', Vector3())
        self.flagNodeAliasName = settings.readString('flagNodeAliasName', '')

# Global variable to store sector base settings
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'
_g_sectorBaseSettings = None

# The main SectorBase class
class SectorBase(BigWorld.Entity):
    _OVER_TERRAIN_HEIGHT = 0.5
    _PLAYER_TEAM_PARAMS = {}
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        # Initialize the base class
        super(SectorBase, self).__init__(self)

        # Initialize member variables
        self.__flagModel = FlagModel()
        self.__terrainSelectedArea = None
        self.capturePercentage = 0
        self.__isCapturedOnStart = False
        self.__baseCaptureSoundObject = None
        self._baseCaptureSirenSoundIsPlaying = False

        # Initialize global sector base settings
        if _g_sectorBaseSettings is None:
            settingsData = ResMgr.openSection(ENVIRONMENT_EFFECTS_CONFIG_FILE + '/sectorBase')
            _g_sectorBaseSettings = _SectorBaseSettingsCache(settingsData)
            SectorBase._PLAYER_TEAM_PARAMS = ((4294901760L, 4286806526L, False), (4278255360L, 4278255360L, True))
        return

    def prerequisites(self):
        # Calculate capture percentage
        self.capturePercentage = float(self.pointsPercentage) / 100

        # Set the initial captured state
        self.__isCapturedOnStart = self.isCaptured

        # Initialize sector base components
        sectorBaseComponent = BigWorld.player().arena.componentSystem.sectorBaseComponent
        if sectorBaseComponent is not None:
            sectorBaseComponent.addSectorBase(self)

        # Initialize assembler for sector base components
        assembler = BigWorld.CompoundAssembler(_g_sectorBaseSettings.flagStaffModelName, self.spaceID)
        assembler.addRootPart(_g_sectorBaseSettings.flagStaffModelName, 'root')

        # Initialize scale matrix
        scaleMatrix = Matrix()
        scaleMatrix.setScale(_g_sectorBaseSettings.flagScale)

        # Add parts to the assembler
        assembler.addPart(_g_sectorBaseSettings.flagModelName, _g_sectorBaseSettings.flagStaffFlagHP, _g_sectorBaseSettings.flagNodeAliasName, scaleMatrix)

        # Prepare return values
        rv = [assembler, _g_sectorBaseSettings.radiusModel]

        # Initialize animation sequence loader if necessary
        if _g_sectorBaseSettings.flagAnim is not None:
            loader = AnimationSequence.Loader(_g_sectorBaseSettings.flagAnim, self.spaceID)
            rv.append(loader)

        # Initialize matrix for positioning
        mProv = Matrix()
        mProv.translation = self.position

        # Initialize base capture sound object
        self.__baseCaptureSoundObject = SoundGroups.g_instance.WWgetSoundObject('base_' + str(self.baseID), mProv)
        self.__baseCaptureSoundObject.play(_g_sectorBaseSettings.baseAttachedSoundEventName)

        return rv

    def onEnterWorld(self, prereqs):
        # Calculate capture percentage
        self.capturePercentage = float(self.pointsPercentage) / 100

        # Set the initial captured state
        if self.__isCapturedOnStart != self.isCaptured:
            self.set_isCaptured(self.__isCapturedOnStart)

        # Initialize sector base components
        sectorBaseComponent = BigWorld.player().arena.componentSystem.sectorBaseComponent
        if sectorBaseComponent is not None:
            sectorBaseComponent.addSectorBase(self)

        # Initialize assembler for sector base components
        assembler = prereqs[_g_sectorBaseSettings.flagStaffModelName]

        # Initialize flag settings
        flagSettings = FlagSettings(prereqs[_g_sectorBaseSettings.flagStaffModelName], _g_sectorBaseSettings.flagNodeAliasName, prereqs[_g_sectorBaseSettings.flagAnim], _g_sectorBaseSettings.flagBackgroundTex, _g_sectorBaseSettings.flagEmblemTex, _g_sectorBaseSettings.flagEmblemTexCoords, self.space
