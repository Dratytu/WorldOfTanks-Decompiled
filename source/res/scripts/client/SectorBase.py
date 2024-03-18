# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/SectorBase.py

import BigWorld # Import BigWorld module for creating and managing game entities
import ResMgr # Import ResMgr module for managing game resources
import SoundGroups # Import SoundGroups module for managing game sounds
from helpers import dependency # Import dependency descriptor for managing object dependencies
from FlagModel import FlagSettings, FlagModel # Import FlagSettings and FlagModel from FlagModel.py
from Math import Vector4, Vector3, Vector2, Matrix # Import various vector and matrix classes from Math.py
from skeletons.account_helpers.settings_core import ISettingsCore # Import ISettingsCore from skeletons.account_helpers.settings_core
from account_helpers.settings_core.settings_constants import GRAPHICS # Import GRAPHICS from settings_constants.py
import AnimationSequence # Import AnimationSequence module for managing animation sequences

# A class to cache sector base settings
class _SectorBaseSettingsCache(object):
    """
    A class for caching sector base settings read from a configuration file.
    """
    def __init__(self, settings):
        """
        Initialize the settings cache with the provided settings data.

        :param settings: A ResMgr.Section instance containing the settings data.
        """
        self.initSettings(settings)

    def initSettings(self, settings):
        """
        Initialize the settings cache with the provided settings data.

        :param settings: A ResMgr.Section instance containing the settings data.
        """
        self.flagModelName = settings.readString('flagModelName', '') # Read the flag model name from the settings data
        self.flagStaffModelName = settings.readString('flagstaffModelName', '') # Read the flagstaff model name from the settings data
        self.radiusModel = settings.readString('radiusModel', '') # Read the radius model name from the settings data
        self.flagAnim = settings.readString('flagAnim', '') # Read the flag animation name from the settings data
        self.flagStaffFlagHP = settings.readString('flagstaffFlagHP', '') # Read the flagstaff flag health point name from the settings data
        self.baseAttachedSoundEventName = settings.readString('wwsound', '') # Read the base attached sound event name from the settings data
        self.flagBackgroundTex = settings.readString('flagBackgroundTex', '') # Read the flag background texture name from the settings data
        self.flagEmblemTex = settings.readString('flagEmblemTex', '') # Read the flag emblem texture name from the settings data
        self.flagEmblemTexCoords = settings.readVector4('flagEmblemTexCoords', Vector4()) # Read the flag emblem texture coordinates from the settings data
        self.flagScale = settings.readVector3('flagScale', Vector3()) # Read the flag scale from the settings data
        self.flagNodeAliasName = settings.readString('flagNodeAliasName', '') # Read the flag node alias name from the settings data

# Global variable to store sector base settings
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml' # Define the environment effects configuration file path
_g_sectorBaseSettings = None # Initialize the global sector base settings variable

# The main SectorBase class
class SectorBase(BigWorld.Entity):
    """
    The main SectorBase class representing a sector base entity in the game world.
    """
    _OVER_TERRAIN_HEIGHT = 0.5 # A constant for the height over terrain
    _PLAYER_TEAM_PARAMS = {} # A dictionary for storing player team parameters
    __settingsCore = dependency.descriptor(ISettingsCore) # A descriptor for the ISettingsCore dependency

    def __init__(self):
        """
        Initialize the SectorBase instance.
        """
        # Initialize the base class
        super(SectorBase, self).__init__(self)

        # Initialize member variables
        self.__flagModel = FlagModel() # Initialize the flag model
        self.__terrainSelectedArea = None # Initialize the terrain selected area
        self.capturePercentage = 0 # Initialize the capture percentage
        self.__isCapturedOnStart = False # Initialize the captured state on start
        self.__baseCaptureSoundObject = None # Initialize the base capture sound object
        self._baseCaptureSirenSoundIsPlaying = False # Initialize the base capture siren sound playing state

        # Initialize global sector base settings
        if _g_sectorBaseSettings is None:
            settingsData = ResMgr.openSection(ENVIRONMENT_EFFECTS_CONFIG_FILE + '/sectorBase') # Open the sector base settings section from the environment effects configuration file
            _g_sectorBaseSettings = _SectorBaseSettingsCache(settingsData) # Initialize the global sector base settings with the settings data
            SectorBase._PLAYER_TEAM_PARAMS = ((4294901760L, 4286806526L, False), (4278255360L, 4278255360L, True)) # Initialize the player team parameters
        return

    def prerequisites(self):
        """
        Perform necessary prerequisites for the sector base.

        :return: A list of prerequisites.
        """
        # Calculate capture percentage
        self.capturePercentage = float(self.pointsPercentage) / 100

        # Set the initial captured state
        self.__isCapturedOnStart = self.isCaptured

        # Initialize sector base components
        sectorBaseComponent = BigWorld.player().arena.componentSystem.sectorBaseComponent # Get the sector base component
        if sectorBaseComponent is not None:
            sectorBaseComponent.addSectorBase(self) # Add the sector base to the sector base component

        # Initialize assembler for sector base components
        assembler = BigWorld.CompoundAssembler(_g_sectorBaseSettings.flagStaffModelName, self.spaceID) # Initialize the assembler with the flag staff model name and space ID
        assembler.addRootPart(_g_sectorBaseSettings.flagStaffModelName, 'root') # Add the root part to the assembler

        # Initialize scale matrix
        scaleMatrix =
