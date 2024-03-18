# Python bytecode 2.7 (decompiled from Python 2.7)

# This script, 'MapActivities.py', contains classes and functions related to map activities in a game.

# Import necessary modules and libraries.
import math
import random
import sys
import BigWorld
import ResMgr
import PlayerEvents
from constants import ARENA_PERIOD
import SoundGroups
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from helpers.PixieBG import PixieBG
from helpers import dependency
from skeletons.map_activities import IMapActivities

# Define a Timer class with static methods to get the current time and initialize the time method.
class Timer:
    __timeMethod = None

    @staticmethod
    def init():
        # Initialize the time method based on whether the game is in server mode or not.
        if BigWorld.serverTime() < 0.0:
            Timer.__timeMethod = BigWorld.time
        else:
            Timer.__timeMethod = BigWorld.serverTime

    @staticmethod
    def getTime():
        # Return the current time using the initialized time method.
        return Timer.__timeMethod()
# End of Timer class

# Define the BaseMapActivity class, an abstract base class for all map activities.
class BaseMapActivity(object):
    # arenaPeriod and name are read-only properties that return the corresponding instance variables.
    @property
    def arenaPeriod(self):
        return self._arenaPeriod

    @property
    def name(self):
        return self._name

    def __init__(self):
        # Initialize instance variables.
        self._startTime = sys.maxint
        self._interval = 0.0
        self._arenaPeriod = 0
        self._name = ''

    def create(self, settings):
        # Create the map activity based on the provided settings. Subclasses should override this method.
        pass

    def destroy(self):
        # Destroy the map activity and release any resources it has allocated. Subclasses should override this method.
        pass

    def start(self):
        # Start the map activity. Subclasses should override this method.
        pass

    def stop(self):
        # Stop the map activity. Subclasses should override this method.
        pass

    def canStart(self):
        # Return True if the map activity can start, False otherwise. Subclasses should override this method.
        return False

    def isActive(self):
        # Return True if the map activity is active, False otherwise. Subclasses should override this method.
        return False

    def isRepeating(self):
        # Return True if the map activity is repeating, False otherwise. Subclasses should override this method.
        return self._interval > 0.0

    def isOver(self):
        # Return True if the map activity is over, False otherwise. Subclasses should override this method.
        return False

    def isPaused(self):
        # Return True if the map activity is paused, False otherwise. Subclasses should override this method.
        return False

    def setStartTime(self, startTime):
        # Set the start time of the map activity. Subclasses should override this method.
        self._startTime = startTime

    # The following methods are helper methods for reading settings and instance variables.
    def _readInterval(self):
        self._interval = self._settings.readFloat('interval', 0.0)

    def _readName(self):
        self._name = self._settings.readString('name', '')
# End of BaseMapActivity class

# Define the MapActivities class, which manages map activities for a game arena.
class MapActivities(IMapActivities):

    def __init__(self):
        # Initialize instance variables and event listeners.
        self.__cbID = None
        self.__isOnArena = False
        self.__pendingActivities = []
        self.__currActivities = []
        self.__arenaPeriod = None
        self.__previousPeriod = None
        PlayerEvents.g_playerEvents.onAvatarBecomePlayer += self.__onAvatarBecomePlayer
        PlayerEvents.g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChange
        PlayerEvents.g_playerEvents.onAvatarBecomeNonPlayer += self.__onAvatarBecomeNonPlayer
        PlayerEvents.g_playerEvents.onAvatarReady += self.__onAvatarReady

    def destroy(self):
        # Destroy the MapActivities object and release any resources it has allocated.
        self.stop()
        PlayerEvents.g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        PlayerEvents.g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange
        PlayerEvents.g_playerEvents.onAvatarBecomeNonPlayer -= self.__onAvatarBecomeNonPlayer
        PlayerEvents.g_playerEvents.onAvatarReady -= self.__onAvatarReady

    def start(self, name, targetTime):
        # Start the specified map activity at the given target time.
        for _, activity in self.__pendingActivities:
            if activity.name == name:
                activity.setStartTime(targetTime)

    def stop(self):
        # Stop all map activities and release any resources they have allocated.
        if self.__cbID is not None:
            BigWorld.cancelCallback(self.__cbID)
            self.__cbID = None
        for activity in self.__currActivities:
            activity.stop()

        for _, activity in self.__pendingActivities:
            activity.stop()

        del self.__currActivities[:]
        del self.__pendingActivities[:]
        return

    def generateOfflineActivities(self, spacePath, usePossibility=True):
        # Generate map activities for an offline game based on the provided space path and a flag to enable randomness.
        xmlName = spacePath.split('/')[-1]
        settings = ResMgr.openSection('scripts/arena_defs/' + xmlName + '.xml/mapActivities')
        chooser = random.uniform if usePossibility else (lambda a, b: (a + b) / 2
