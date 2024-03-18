# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleBerserkerComponent.py

# Import necessary modules and constants
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

# Subclass VehicleAbilityBaseComponent to create VehicleBerserkerComponent
class VehicleBerserkerComponent(VehicleAbilityBaseComponent):
    # Define class variables for equipment name, timer view ID, and marker ID
    __EQUIPMENT_NAME = BattleRoyaleEquipments.BERSERKER
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.BERSERKER
    __MARKER_ID = BATTLE_MARKER_STATES.BERSERKER_STATE

    # Initialize the component, setting id, superclass, and timer/marker details
    def __init__(self):
        self.__id = id(self)
        super(VehicleBerserkerComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    # Override the updateTimer method to update the timer and send equipment component updated event
    def _updateTimer(self, data):
        # Set tickInterval in the data dictionary
        data['tickInterval'] = self.tickInterval
        # Call the superclass method to update the timer
        super(VehicleBerserkerComponent, self)._updateTimer(data)
        # Send equipment component updated event to the vehicle's guiSessionProvider
        self.entity.guiSessionProvider.shared.vehicleState.onEquipmentComponentUpdated(self.__EQUIPMENT_NAME, self.entity.id, data)

