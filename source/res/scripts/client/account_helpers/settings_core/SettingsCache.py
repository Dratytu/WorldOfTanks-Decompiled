# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/settings_core/SettingsCache.py

from Event import Event  # Importing Event class from the Event module
from adisp import adisp_async  # Importing adisp_async decorator
from gui.ClientUpdateManager import g_clientUpdateManager  # Importing g_clientUpdateManager from the ClientUpdateManager module
from gui.shared.utils.requesters.IntSettingsRequester import IntSettingsRequester  # Importing IntSettingsRequester from the IntSettingsRequester module
from account_helpers.settings_core.settings_constants import VERSION  # Importing VERSION constant from the settings_constants module
from skeletons.account_helpers.settings_core import ISettingsCache  # Importing ISettingsCache interface

class SettingsCache(ISettingsCache): 
