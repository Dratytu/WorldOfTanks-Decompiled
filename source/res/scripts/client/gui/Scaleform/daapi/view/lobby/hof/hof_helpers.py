# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hof/hof_helpers.py

import logging
import Keys  # Importing Keys from gui.System.keys
from helpers import dependency
from gui import GUI_SETTINGS, DialogsInterface  # Importing DialogsInterface from gui.Scaleform.genConsts.PROFILE_CONSTANTS and GUI_SETTINGS from gui
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS  # PROFILE_CONSTANTS imported for button IDs
from skeletons.gui.lobby_context import ILobbyContext  # Skeleton for lobby context
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NEW_HOF_COUNTER

_logger = logging.getLogger(__name__)
NEW_HOF_BUTTONS_IDS = (PROFILE_CONSTANTS.HOF_ACHIEVEMENTS_BUTTON, PROFILE_CONSTANTS.HOF_VEHICLES_BUTTON)
NEW_ACHIEVEMENTS_BUTTONS_IDS = (PROFILE_CONSTANTS.HOF_ACHIEVEMENTS_BUTTON, PROFILE_CONSTANTS.HOF_VEHICLES_BUTTON, PROFILE_CONSTANTS.HOF_VIEW_RATING_BUTTON)

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)  # Decorator to replace None lobbyContext with a default one
def _getHofUrl(urlName, lobbyContext=None):  # Function to get the HoF URL with a given name
    if lobbyContext is None:
        return
    else:
        try:
            return lobbyContext.getServerSettings().bwHallOfFame.hofHostUrl + GUI_SETTINGS.hallOfFame.get(urlName)
        except (AttributeError, TypeError):
            _logger.exception('_getHofUrl() error')
            return

        return


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def isHofEnabled(lobbyContext=None):  # Function to check if HoF is enabled
    if lobbyContext is None:
        return
    else:
        try:
            return lobbyContext.getServerSettings().isHofEnabled()
        except (AttributeError, TypeError):
            _logger.exception('isHofEnabled() error')
            return

        return


# Helper functions to get HoF URLs
def getHofAchievementsRatingUrl():
    return _getHofUrl('achievementsRatingUrl')


def getHofAchievementsStatisticUrl():
    return _getHofUrl('achievementsStatisticUrl')


def getHofVehiclesRatingUrl():
    return _getHofUrl('vehiclesRatingUrl')


def getHofVehiclesStatisticUrl():
    return _getHofUrl('vehiclesStatisticUrl')


def getHofRatingUrlForVehicle(vehicleCD):  # Function to get the HoF rating URL for a specific vehicle
    if vehicleCD is None:
        _logger.debug('vehicleCD should be not None')
        return
    else:
        try:
            return _getHofUrl('vehiclesRatingUrl') + '/' + str(vehicleCD)
        except TypeError:
            _logger.exception('getHofRatingUrlForVehicle() error')
            return

        return


# Functions to calculate and get counters for new HoF tabs
def _calculateCounters(ids):
    count = 0
    for cID in ids:
        if isHofButtonNew(cID):
            count += 1

    return count


def getAchievementsTabCounter():
    return _calculateCounters(NEW_ACHIEVEMENTS_BUTTONS_IDS)


def getTabCounter():
    return int(getHofTabCounter() > 0) + _calculateCounters((PROFILE_CONSTANTS.HOF_VIEW_RATING_BUTTON,))


def getHofTabCounter():
    return _calculateCounters(NEW_HOF_BUTTONS_IDS)


def isHofButtonNew(buttonID):  # Function to check if a HoF button is new
    return _getSettingsFromStorage().get(buttonID)


def setHofButtonOld(buttonID):  # Function to set a HoF button as old
    settings = _getSettingsFromStorage()
    if buttonID in settings.keys():
        settings[buttonID] = False
        _setSettingsToStorage(settings)


def _getSettingsFromStorage():  # Function to get settings from storage
    return AccountSettings.getCounters(NEW_HOF_COUNTER)


def _setSettingsToStorage(value):  # Function to set settings to storage
    AccountSettings.setCounters(NEW_HOF_COUNTER, value)


# Functions to handle disabled keys and show a dialog
def getHofDisabledKeys():
    return ((Keys.KEY_F5,
      True,
      False,
      False,
      False),
     (Keys.KEY_LEFTARROW,
      True,
      True,
      False,
      False),
     (Keys.KEY_NUMPAD4,
      True,
      True,
      False,
      False),
     (Keys.KEY_RIGHTARROW,
      True,
      True,
      False,
      False),
     (Keys.KEY_NUMPAD6,
      True,
      True,
      False,
      False),
     (Keys.KEY_BACKSPACE,
      True,
      False,
      True,
      False),
     (Keys.KEY_F5,
      True,
      False,
      False,
      True),
     (Keys.KEY_HOME,
      True,
      True,
      False,
      False),
     (Keys.KEY_NUMPAD7,
      True,
      True,
      False,
      False),
     (Keys.KEY_0,

