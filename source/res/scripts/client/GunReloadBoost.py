# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/GunReloadBoost.py

# Importing required modules
from cache import cached_property  # A decorator to cache the result of a method with a unique key
from helpers import dependency  # A module to manage object dependencies
from skeletons.gui.battle_session import IBattleSessionProvider  # A skeleton (interface) for the battle session provider
from view_state_component import ViewStateComponent  # A component for managing view states

# Define the GunReloadBoost class, which inherits from ViewStateComponent
class GunReloadBoost(ViewStateComponent):

    # Define a cached property for the _sessionProvider
    @cached_property
    def _sessionProvider(self):
        # Return the IBattleSessionProvider instance using dependency injection
        return dependency.instance(IBattleSessionProvider)

    # onReloadBoost method
    def onReloadBoost(self):
        # Import VEHICLE_VIEW_STATE from battle_constants
        from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
        
        # Check if the entity ID matches the controlling vehicle ID
        if self.entity.id == self._sessionProvider.shared.vehicleState.getControllingVehicleID():
            # Invalidate the vehicle state for GUN_RELOAD_BOOST
            self._sessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.GUN_RELOAD_BOOST, None)
        
        # Return None
        return
