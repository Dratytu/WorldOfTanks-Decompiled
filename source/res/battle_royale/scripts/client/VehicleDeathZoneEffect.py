# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleDeathZoneEffect.py

# Import necessary modules and libraries
import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from death_zones_helpers import ZONE_STATE
from constants import DEATH_ZONES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, DeathZoneTimerViewState
from battle_royale.gui.battle_control.battle_constants import BrTimerViewState
from script_component.DynamicScriptComponent import DynamicScriptComponent

# Define the VehicleDeathZoneEffect class, which inherits from DynamicScriptComponent
class VehicleDeathZoneEffect(DynamicScriptComponent):
    # Define a dependency for IBattleSessionProvider using dependency.descriptor
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Define a method called _onAvatarReady
    def _onAvatarReady(self):
        # Call the set_state method when the avatar is ready
        self.set_state()

    # Define the set_state method
    def set_state(self, _=None):
        # Calculate the time left in the death zone
        timeLeft = self.timeLeft()
        # Create a DeathZoneTimerViewState object with the appropriate parameters
        value = DeathZoneTimerViewState(DEATH_ZONES.STATIC, False, timeLeft, BrTimerViewState.fromZone(self.state), timeLeft + BigWorld.serverTime())
        # Invalidate the vehicle state for DEATHZONE_TIMER with the new value
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.DEATHZONE_TIMER, value)

    # Define the timeLeft method
    def timeLeft(self):
        # If the state is CRITICAL, calculate the time left based on the timeToDamage and damageTime variables
        if self.state == ZONE_STATE.CRITICAL:
            if self.timeToDamage > 0:
                return self.timeToDamage
            return max(self.damageTime - BigWorld.serverTime(), 0.0)

    # Define the onDamaged method
    def onDamaged(self):
        # Create a DeathZoneTimerViewState object with the appropriate parameters
        value = DeathZoneTimerView
