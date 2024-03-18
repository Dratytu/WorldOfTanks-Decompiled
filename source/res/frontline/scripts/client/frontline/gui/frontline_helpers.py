# frontline/scripts/client/frontline/gui/frontline_helpers.py

# Import necessary modules and packages
import typing
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_container_tab_model import TabType
from gui.periodic_battles.models import PrimeTimeStatus
from helpers import time_utils, dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

# Define a decorator function to replace None values in kwargs with default values
@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def geFrontlineState(withPrimeTime=False, epicController=None):
    # Get the current local server timestamp
    now = time_utils.getCurrentLocalServerTimestamp()
    # Get the start date and end date of the Frontline season
    startDate, endDate = epicController.getSeasonTimeRange()
    # Check if the current time is after the end date of the season
    if now > endDate:
        # If so, get the current season and its end date
        season = epicController.getCurrentSeason()
        endSeasonDate = season.getEndDate() if season else 0
        # Return the FrontlineState as FINISHED along with the end season date and remaining time
        return (FrontlineState.FINISHED, endSeasonDate, int(endSeasonDate - now))
    # Check if the current time is before the start date of the season
    if now < startDate:
        # If so, return the FrontlineState as ANNOUNCE along with the start date and remaining time
        return (FrontlineState.ANNOUNCE, startDate, int(startDate - now))
    # Get the prime time status, time left, and other information
    primeTimeStatus, timeLeft, _ = epicController.getPrimeTimeStatus()
    # Check if the prime time status is not AVAILABLE
    if primeTimeStatus is not PrimeTimeStatus.AVAILABLE:
        # If not, check if the withPrimeTime argument is True
        if withPrimeTime:
            # If so, return the FrontlineState as FROZEN along with the end time and remaining time
            return (FrontlineState.FROZEN, int(now + timeLeft), timeLeft)
        # If withPrimeTime is False, return the FrontlineState as FROZEN along with the end date and remaining time
        return (FrontlineState.FROZEN, endDate, int(endDate - now))
    # If the prime time status is AVAILABLE, return the FrontlineState as ACTIVE along with the end date and remaining time
    return (FrontlineState.ACTIVE, endDate, int(endDate - now))

# Define a function to get the FrontlineStates that make the hangar unavailable
def getStatesUnavailableForHangar():
    return [FrontlineState.FINISHED, FrontlineState.ANNOUNCE]

# Define a
