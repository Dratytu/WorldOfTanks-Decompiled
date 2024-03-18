# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/poi_helpers.py

import typing  # For type hinting (if typing.TYPE_CHECKING is True)
import BigWorld  # For accessing server time and other game world services
from items import vehicles  # For accessing vehicle equipment cache
from points_of_interest_shared import PoiEquipmentNamesByPoiType, PoiTypesByPoiEquipmentName  # For mapping point of interest types to equipment names and vice versa

# If type checking is enabled, the following modules are expected
if typing.TYPE_CHECKING:
    from items.artefacts import Equipment  # For Equipment class
    from points_of_interest.components import PoiStateComponent  # For PoiStateComponent class

def getPoiCooldownProgress(poiState):
    """
    Calculates the progress of a point of interest's cooldown as a percentage.

    :param poiState: The PoiStateComponent instance representing the point of interest's state
    :return: A float representing the cooldown progress in percentage (0.0 to 100.0)
    """
    status = poiState.status  # Get the status of the point of interest
    duration = status.endTime - status.startTime  # Calculate the duration of the cooldown
    progress = (BigWorld.serverTime() - status.startTime) / duration * 100  # Calculate the progress of the cooldown
    return progress


def getPoiEquipmentByType(poiType):
    """
    Retrieves the Equipment instance associated with a given point of interest type.

    :param poiType: The point of interest type (str)
    :return: The Equipment instance or None if not found
    """
    cache = vehicles.g_cache  # Get the vehicle equipment cache
    name = PoiEquipmentNamesByPoiType[poiType]  # Get
