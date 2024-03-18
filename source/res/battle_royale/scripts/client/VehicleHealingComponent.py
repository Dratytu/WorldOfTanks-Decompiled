# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleHealingComponent.py

# Import necessary modules
import BigWorld
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

# Define the VehicleHealingComponent class, which inherits from VehicleAbilityBaseComponent
class VehicleHealingComponent(VehicleAbilityBaseComponent):
    # Define class variables for timer view ID and marker ID
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.HEALING
    __MARKER_ID = BATTLE_MARKER_STATES.HEALING_STATE

    # Constructor for the VehicleHealingComponent class
    def __init__(self):
        # Initialize _isDestroying as False
        self._isDestroying = False
        # Call the constructor of the parent class with self.__TIMER_VIEW_ID and self.__MARKER_ID
        super(VehicleHealingComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    # Define set_isInactivation method
    def set_isInactivation(self, prev):
        # Call the private method _updateVisuals
        self._updateVisuals()

    # Define _updateTimer method
    def _updateTimer(self, data):
        # Update data dictionary with isInactivation and isSourceVehicle
        data.update({'isInactivation': self.isInactivation,
                     'isSourceVehicle': self.getIsSourceVehicle()})
        # Call the parent class's _updateTimer method with updated data
        super(VehicleHealingComponent, self)._updateTimer(data)

    # Define _updateMarker method
    def _updateMarker(self, data, isHide=False
