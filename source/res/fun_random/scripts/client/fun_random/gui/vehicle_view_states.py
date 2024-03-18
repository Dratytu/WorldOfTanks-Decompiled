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
        """
        Checks if the given vehicle is suitable for fun random battles.

        :param vehicle: The vehicle to check.
        :return: True if the vehicle is only for fun random battles, False otherwise.
        """
        return vehicle.item.isOnlyForFunRandomBattles

