# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/progression_helpers.py

import binascii
import logging
import struct
from collections import namedtuple

# Dependency injection for IItemsCache
from CurrentVehicle import g_currentVehicle
from constants import EVENT_TYPE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events import formatters
from gui.server_events.events_helpers import MISSIONS_STATES
from helpers import dependency
from helpers import int2roman
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache

# Logger setup for this module
_logger = logging.getLogger(__name__)

def makeEventID(itemIntCD, vehicleIntCD):
    """
    Creates a unique event ID for customization progression using the itemIntCD and vehicleIntCD.

    :param int itemIntCD: The integer CD of the item.
    :param int vehicleIntCD: The integer CD of the vehicle.
    :return str: The hexadecimal formatted event ID.
    """
    return binascii.hexlify(struct.pack('II', itemIntCD, vehicleIntCD))


def parseEventID(eventID):
    """
    Parses a customization progression event ID and returns the itemIntCD and vehicleIntCD.

    :param str eventID: The hexadecimal formatted event ID.
    :return tuple: The itemIntCD and vehicleIntCD as integers.
    """
    return struct.unpack('II', binascii.unhexlify(eventID))


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getProgressionPostBattleInfo(itemIntCD, vehicleIntCD, progressionData, itemsCache=None):
    """
    Retrieves the customization progression post-battle information for the given itemIntCD, vehicleIntCD, and progressionData.

    :param int itemIntCD: The integer CD of the item.
    :param int vehicleIntCD: The integer CD of the vehicle.
    :param dict progressionData: The progression data for the item.
    :param IItemsCache itemsCache: The items cache instance (optional).
    :return dict: The customization progression post-battle information.
    """
    vehicle = itemsCache.items.getItemByCD(vehicleIntCD)
    item = itemsCache.items.getItemByCD(itemIntCD)
    level = progressionData.get('level')

    # Early return if level is None
    if level is None:
        return

    progress = progressionData.get('progress')
    inProgress = progress is not None

    # Generate the status tooltip based on the level
    if level > 1:
        statusTooltip = backport.text(R.strings.tooltips.quests.status.customizationProgression.done(), name=item.userName, level=int2roman(level))
    else:
        statusTooltip = backport.text(R.strings.tooltips.quests.status.customizationProgression.doneFirst(), name=item.userName)

    # Prepare the quest info dictionary
    questInfo = {
        'questID': makeEventID(itemIntCD, vehicleIntCD),
        'eventType': EVENT_TYPE.C11N_PROGRESSION,
        'status': MISSIONS_STATES.IN_PROGRESS if inProgress else MISSIONS_STATES.COMPLETED,
        'description': backport.text(R.strings.battle_results.customizationProgress.descr(), level=int2roman(level + 1) if inProgress else int2roman(level), name=item.userName),
        'statusTooltip': statusTooltip
    }

    # Get the link button parameters
    isLinkEnabled, linkBtnTooltip = getC11nProgressionLinkBtnParams(vehicle)

    # Prepare the info dictionary
    info = {
        'questInfo': questInfo,
        'linkBtnEnabled': isLinkEnabled,
        'linkBtnTooltip': backport.text(linkBtnTooltip)
    }

    # Add progress list or awards based on the progress state
    if inProgress:
        info['progressList'] = __makeProgressList(item, level, progressionData)
    else:
        info['awards'] = __makeAwardsVO(item, level, vehicleIntCD)

    return info


# Namedtuple for C11nProgressionLinkBtnParams
C11nProgressionLinkBtnParams = namedtuple('C11nProgressionLinkBtnParams', ('isLinkEnabled', 'linkBtnTooltip'))

def getC11nProgressionLinkBtnParams(vehicle):
    """
    Gets the customization progression link button parameters for the given vehicle.

    :param vehicle: The vehicle instance.
    :return namedtuple: The namedtuple containing isLinkEnabled and linkBtnTooltip.
    """
    isLinkEnabled = vehicle.isCustomizationEnabled() if vehicle is not None else False
    linkBtnTooltip = R.strings.tooltips.quests.linkBtn.customizationProgression
    linkBtnTooltip = linkBtnTooltip.enabled() if isLinkEnabled else linkBtnTooltip.disabled()
    return C11nProgressionLinkBtnParams(isLinkEnabled, linkBtnTooltip)


def getC11n2dProgressionLinkBtnParams():
    """
    Gets the customization progression link button parameters for the current vehicle.

    :return namedtuple: The namedtuple containing isLinkEnabled and linkBtnTooltip.
    """
    return getC11nProgressionLinkBtnParams(g_currentVehicle.item)


def __makeAwardsVO(item, level, vehicleIntCD):
    """
    Creates the awards VO for the given item, level, and vehicleIntCD.

    :param item: The item instance.
    :param int level: The level of the item.
    :param int vehicleIntCD
