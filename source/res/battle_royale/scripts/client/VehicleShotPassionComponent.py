# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleShotPassionComponent.py
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

class VehicleShotPassionComponent(VehicleAbilityBaseComponent):
    EQUIPMENT_NAME = BattleRoyaleEquipments.SHOT_PASSION
    TIMER_VIEW_ID = VEHICLE_VIEW_STATE.SHOT_PASSION
    MARKER_ID = BATTLE_MARKER_STATES.SHOT_PASSION_STATE

    def __init__(self):
        super(VehicleShotPassionComponent, self).__init__(self.TIMER_VIEW_ID, self.MARKER_ID)
        self._data = None

    def set_stage(self, prev):
        self._update_timer(None)
        return

    def get_info(self):
        data = self._get_timer_data()
        data['stage'] = self.stage
        return data

    def _update_timer(self, data):
        if data is None:
            data = self._get_timer_data()
        data['stage'] = self.stage
        super(VehicleShotPassionComponent, self)._update_timer(data)
        self._gui_session_provider.shared.vehicle_state.on_equipment_component_updated(self.EQUIPMENT_NAME, self.entity.id, data)

    @property
    def _gui_session_provider(self):
        return super(VehicleShotPassionComponent, self)._gui_session_provider

