# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/settings_core/SettingsCache.py

# Importing Event class from the Event module
from Event import Event 

# Importing adisp_async decorator
from adisp import adisp_async 

# Importing g_clientUpdateManager from the ClientUpdateManager module
from gui.ClientUpdateManager import g_clientUpdateManager 

# Importing IntSettingsRequester from the IntSettingsRequester module
from gui.shared.utils.requesters.IntSettingsRequester import IntSettingsRequester 

# Importing VERSION constant from the settings_constants module
from account_helpers.settings_core.settings_constants import VERSION 

# Importing ISettingsCache interface
from skeletons.account_helpers.settings_core import ISettingsCache 

# Defining the SettingsCache class that implements the ISettingsCache interface
class SettingsCache(ISettingsCache):
