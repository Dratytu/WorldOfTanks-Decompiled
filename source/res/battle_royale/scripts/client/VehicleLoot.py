# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleLoot.py

import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from constants import LootAction
from debug_utils import LOG_DEBUG_DEV

class VehicleLoot(BigWorld.DynamicScriptComponent):
    """
    A class representing a loot component for a vehicle in a battle royale game mode.
    """

    def __invalidateState(self, action, time):
        """
        Internal method to invalidate the loot state of the vehicle.

        :param action: The loot action to be taken.
        :param time: The time at which the action is to be taken.
        """
        LOG_DEBUG_DEV('__invalidateState', self.lootID, self.lootTypeID, action, time)
        self.entity.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.LOOT, (self.lootID,
                                                                                        self.lootTypeID,
                                                                                        action,
                                                                                        time))

    def __init__(self):
        """
        Initializes the VehicleLoot component.
        """
        super(VehicleLoot, self).__init__()
        if self.pickupTotalTime:
            total_time = self.pickupTotalTime
        else:
            total_time = max(self.pickupEndTime - BigWorld.serverTime(), 0)
        self.__invalidateState(LootAction.PICKUP_STARTED, total_time)

    def onDestroy(self):
        """
        Called when the VehicleLoot component is destroyed.
        """
        if self.pickupEndTime > 0:
            self.__invalidateState(LootAction.PICKUP_FAILED, 0)
        else:
            self.__invalidateState(LootAction.PICKUP_SUC
