# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/vehicle_view_states.py

# Import necessary classes and functions from fun_random and gui packages
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.vehicle_view_states import SelectedViewState

# Define FunRandomVehicleViewState class that inherits from SelectedViewState and FunSubModesWatcher
class FunRandomVehicleViewState(SelectedViewState, FunSubModesWatcher):

    # Class method to check if the given vehicle is suitable for fun random battles
    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return vehicle.item.isOnlyForFunRandomBattles

    # Setter method for customizationVisible attribute
    def setCustomizationVisible(self, customizationVisible):
        self._isCustomizationVisible = customizationVisible

    # Setter method for eliteShown attribute
    def setEliteShown(self, eliteShown):
        self._isEliteShown = eliteShown

    # Setter method for levelShown attribute
    def setLevelShown(self, levelShown):
        self._isLevelShown = levelShown

    # Setter method for maintenanceVisible attribute
    def setMaintenanceVisible(self, maintenanceVisible):
        self._isMaintenanceVisible = maintenanceVisible

    # Setter method for roleShown attribute
    def setRoleShown(self, roleShown):
        self._isRoleShown = roleShown

    # Method to resolve the vehicle state based on the current sub-mode
    def _resolveVehicleState(self, vehicle):
        super(FunRandomVehicleViewState, self)._resolveVehicleState(vehicle)
        self.__resolveStateByCurrentSubMode(vehicle)

    # Method to resolve the vehicle view state based on the desired sub-mode
    @hasDesiredSubMode()
    def __resolveStateByCurrentSubMode
