# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleSelfBuffComponent.py

# Import necessary modules
import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

# Define class level constants
class VehicleSelfBuffComponent(VehicleAbilityBaseComponent):
    __EQUIPMENT_NAME = BattleRoyaleEquipments.SELF_BUFF
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.INSPIRE
    __MARKER_ID = BATTLE_MARKER_STATES.INSPIRING_STATE

    def __init__(self):
        # Initialize the superclass with the timer view ID and marker ID
        super(VehicleSelfBuffComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _updateTimer(self, data):
        # Get the duration of the self-buff
        duration = self._getDuration()

        # Calculate whether the timer should be hidden or not
        isHide = self.entity.id != BigWorld.player().getObservedVehicleID() or duration == 0

        # Update the end time and isInactivation status in the data dictionary
        data['endTime'] = 0.0 if isHide else self.finishTime
        data['isInactivation'] = None if isHide else duration > 0

        # Set the isSourceVehicle flag to True
        data['isSourceVehicle'] = True

        # Call the superclass's implementation of _updateTimer
        super(VehicleSelfBuffComponent, self)._updateTimer(data)
