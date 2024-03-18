# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: battle_royale/scripts/client/vehicle_corroding_shot_component.py
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from vehicle_ability_base_component import VehicleAbilityBaseComponent

class VehicleCorrodingShotComponent(VehicleAbilityBaseComponent):
    TIMER_VIEW_ID = VEHICLE_VIEW_STATE.CORRODING_SHOT

    def __init__(self, *args):
        super().__init__(self.TIMER_VIEW_ID)

