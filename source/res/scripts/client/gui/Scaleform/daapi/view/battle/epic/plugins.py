# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/plugins.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES

# Define a tuple of priority values for epic status effects
_EPIC_STATUS_EFFECTS_PRIORITY = (
    BATTLE_MARKER_STATES.STUN_STATE,        # 0: Stun state
    BATTLE_MARKER_STATES.FL_REGENERATION_KIT_STATE,  # 1: Regeneration kit state
    BATTLE_MARKER_STATES.REPAIRING_STATE,   # 2: Repairing state
    BATTLE_MARKER_STATES.ENGINEER_STATE,    # 3: Engineer state
    BATTLE_MARKER_STATES.HEALING_STATE,     # 4: Healing state
    BATTLE_MARKER_STATES.BERSERKER_STATE,   # 5: Berserker state
    BATTLE_MARKER_STATES.STEALTH_STATE,     # 6: Stealth state
    BATTLE_MARKER_STATES.INSPIRING_STATE,   # 7: Inspiring state
    BATTLE_MARKER_STATES.DEBUFF_STATE,      # 8: Debuff state
    BATTLE_MARKER_STATES.INSPIRED_STATE     # 9: Inspired state
)

# Subclass VehicleMarkerPlugin to create EpicVehicleMarkerPlugin
class EpicVehicleMarkerPlugin(VehicleMarkerPlugin):

    # Override the _getMarkerStatusPriority method
    def _getMarkerStatusPriority(self, markerState):
        """
        Return the priority of the given marker
