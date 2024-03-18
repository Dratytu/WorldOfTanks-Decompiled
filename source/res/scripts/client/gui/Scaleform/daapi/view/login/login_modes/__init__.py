# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/__init__.py

import typing  # For type checking

from gui import GUI_SETTINGS  # Access global settings related to the GUI
from skeletons.gui.login_manager import ILoginManager  # Interface for the login manager
from helpers import dependency  # For dependency injection

# Import specific login modes
from wgc_mode import WgcMode
from steam_mode import SteamMode
from credentials_mode import CredentialsMode
from social_mode import SocialMode

# Only needed if type checking is enabled
if typing.TYPE_CHECKING:
    from base_mode import BaseMode

@dependency.replace_none_kwargs(loginManager=ILoginManager)  # Inject ILoginManager instance
def createLoginMode(view, loginManager=None):
    """
    Factory function to create the appropriate login mode based on the given conditions.

    :param view: The view object to be used in the login mode
    :param loginManager: ILoginManager instance (dependency injected)
    :return: An instance of the appropriate login mode
    """
    if loginManager.isWgcSteam:
        return SteamMode(view)  # Return SteamMode if WGC and Steam are enabled

    mode = CredentialsMode(view)  # Initialize the login process with CredentialsMode

    if GUI_SETTINGS.socialNetworkLogin['enabled']:
        mode = SocialMode(view, mode)  # If social network login is enabled, wrap the mode with SocialMode

    if loginManager.wgcAvailable:
        mode = WgcMode(view, mode)  # If WGC is available, wrap the mode with WgcMode

    return mode  # Return the final initialized login mode
