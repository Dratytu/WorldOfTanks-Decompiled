# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/Settings.py

import BigWorld

# The global instance of the Settings class
g_instance = None

# Constants for various settings keys
KEY_CONTROL_MODE = 'controlMode'
KEY_LOGIN_INFO = 'loginInfo'
KEY_SCREEN_SIZE = 'screenSize'
KEY_VIDEO_MODE = 'videoMode'
KEY_LOBBY_TOOLTIP_DELAY = 'lobbyTooltipDelay'
KEY_SOUND_PREFERENCES = 'soundPrefs'
KEY_REPLAY_PREFERENCES = 'replayPrefs'
APPLICATION_CLOSE_DELAY = 'closeApplicationDelay'
KEY_MESSENGER_PREFERENCES = 'messengerPrefs'
KEY_ACCOUNT_SETTINGS = 'accounts'
KEY_COMMAND_MAPPING = 'commandMapping'
KEY_SHOW_STARTUP_MOVIE = 'showStartupMovie'
KEY_VOIP_DEVICE = 'captureDevice'
KEY_ENABLE_EDGE_DETECT_AA = 'enableEdgeDetectAA'
KEY_WINDOWS_STORED_DATA = 'windowsStoredData'
KEY_FOV = 'fov'
KEY_GUI_NOTIFY_INFO = 'guiNotifyInfo'
KEY_DYNAMIC_FOV = 'dynamicFov'
KEY_DYNAMIC_FOV_ENABLED = 'dynamicFovEnabled'
IGB_HARDWARE_ACCELERATION_ENABLED = 'igbHardwareAccelerationEnabled'
INTRO_VIDEO_VERSION = 'introVideoVersion'
VIDEO_BUFFERING_TIME = 'videoBufferingTime'
KEY_BOOTCAMP_PREFERENCES = 'bootcampPrefs'
POPUPS_WINDOWS_DISABLED = 'popupsWindowsDisabled'
KEY_MAPS_TRAINING_PREFERENCES = 'mapsTraining'

class Settings(object):
    """
    A class representing the game settings.
    Handles saving the settings to the preferences.
    """

    def __init__(self, scriptConfig, engineConfig, userPrefs):
        """
        Initializes a new Settings instance.

        :param scriptConfig: The script configuration.
