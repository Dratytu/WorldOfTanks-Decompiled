# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_results/components/comp7.py

from comp7_ranks_common import EXTRA_RANK_TAG # Importing EXTRA_RANK_TAG constant from comp7_ranks_common module
from constants import EntityCaptured, FAIRPLAY_VIOLATIONS # Importing EntityCaptured and FAIRPLAY_VIOLATIONS constants from constants module
from gui.Scaleform.genConsts.COMP7_CONSTS import COMP7_CONSTS # Importing COMP7_CONSTS constants from COMP7_CONSTS module
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS # Importing TOOLTIPS_CONSTANTS constants from TOOLTIPS_CONSTANTS module
from gui.battle_results.components import base, style # Importing base and style modules from battle_results.components package
from gui.battle_results.components.vehicles import RegularVehicleStatValuesBlock, RegularVehicleStatsBlock, TeamStatsBlock, _getStunFilter # Importing RegularVehicleStatValuesBlock, RegularVehicleStatsBlock, TeamStatsBlock, and _getStunFilter functions from vehicles module
from gui.battle_results.settings import PLAYER_TEAM_RESULT # Importing PLAYER_TEAM_RESULT constant from settings module

def checkIfDeserter(reusable): # Function to check if the player is a deserter
    """
    Checks if the player has a desertion penalty.

    :param reusable: The reusable object containing player information
    :return: True if the player is a deserter, False otherwise
    """
    if not reusable.personal.avatar.hasPenalties():
        return False
    penaltyName, _ = reusable.personal.avatar.getPenaltyDetails()
    return penaltyName == FAIRPLAY_VIOLATIONS.COMP7_DESERTER


def checkIsQualificationBattle(personalRecord): # Function to check if the battle is a qualification battle
    """
    Checks if the battle is a qualification battle for COMP7.

    :param personalRecord: The personal record of the player in the battle
    :return: True if the battle is a qualification battle, False otherwise
    """
    return personalRecord['avatar'].get('comp7QualActive', False) if 'avatar' in personalRecord else False


def getFormattedRating(rating): # Function to format the rating
    """
    Formats the rating as a string with a '+' or '-' sign.

    :param rating: The rating value
    :return: The rating as a formatted string
    """
    return '{:+}'.format(rating)

# Other classes and functions in the code
