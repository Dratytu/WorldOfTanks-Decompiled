# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/battle_royale/consumables_panel.py
from constants import EQUIPMENT_STAGES
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class BattleRoyaleConsumablesPanel(ConsumablesPanel):
    _PANEL_MAX_LENGTH = 10
    _AMMO_START_IDX = 0
    _AMMO_END_IDX = 1
    _EQUIPMENT_START_IDX = 2
    _EQUIPMENT_END_IDX = 9
    _EQUIPMENT_ICON_PATH = '../maps/icons/battleRoyale/artefact/%s.png'

    def __init__(self):
        super(BattleRoyaleConsumablesPanel, self).__init__()
        self.__quantityMap = [None] * self._PANEL_MAX_LENGTH
        return

    def as_resetS(self):
        pass

    def _populate(self):
        super(BattleRoyaleConsumablesPanel, self)._populate()
        vehStateCtrl = self.sessionProvider.shared.vehicleState
        if vehStateCtrl is not None:
            vehStateCtrl.onVehicleStateUpdated += self.__onVehicleLootAction
        return

    def _dispose(self):
        vehStateCtrl = self.sessionProvider.shared.vehicleState
        if vehStateCtrl is not None:
            vehStateCtrl.onVehicleStateUpdated -= self.__onVehicleLootAction
        super(BattleRoyaleConsumablesPanel, self)._dispose()
        return

    def _getPanelSettings(self):
        return CONSUMABLES_PANEL_SETTINGS.BATTLE_ROYALE_SETTINGS_ID

    def _onShellsAdded(self, intCD, descriptor, quantity, _, gunSettings):
        if intCD in self._cds:
            return
        else:
            slotIdx = self.__getNewSlotIdx(self._AMMO_START_IDX, self._AMMO_END_IDX)
            if slotIdx is None:
                return
            self._addShellSlot(slotIdx, intCD, descriptor, quantity, gunSettings)
            self._mask |= 1 << slotIdx
            return

    def _onShellsUpdated(self, intCD, quantity, *args):
        if intCD not in self._cds:
            return
        super(BattleRoyaleConsumablesPanel, self)._onShellsUpdated(intCD, quantity, *args)

    def _onNextShellChanged(self, intCD):
        if intCD not in self._cds:
            return
        super(BattleRoyaleConsumablesPanel, self)._onNextShellChanged(intCD)

    def _onCurrentShellChanged(self, intCD):
        if intCD not in self._cds:
            return
        super(BattleRoyaleConsumablesPanel, self)._onCurrentShellChanged(intCD)

    def _onGunSettingsSet(self, _):
        self.__resetShellSlots()
        self._resetDelayedReload()

    def _onGunReloadTimeSet(self, currShellCD, state):
        if currShellCD not in self._cds:
            return
        super(BattleRoyaleConsumablesPanel, self)._onGunReloadTimeSet(currShellCD, state)

    def _onEquipmentAdded(self, intCD, item):
        if item is None or intCD in self._cds:
            return
        else:
            slotIdx = self.__getNewSlotIdx(self._EQUIPMENT_START_IDX, self._EQUIPMENT_END_IDX)
            if slotIdx is None:
                return
            self._addEquipmentSlot(slotIdx, intCD, item)
            self._mask |= 1 << slotIdx
            return

    def _isAvatarEquipment(self, item):
        return False

    def _addOptionalDeviceSlot(self, idx, intCD, descriptor, isActive):
        pass

    def _updateShellSlot(self, idx, quantity):
        super(BattleRoyaleConsumablesPanel, self)._updateShellSlot(idx, quantity)
        prevQuantity = self.__quantityMap[idx]
        self.__quantityMap[idx] = quantity
        if prevQuantity is not None and quantity > prevQuantity:
            self.as_setGlowS(idx, CONSUMABLES_PANEL_SETTINGS.GLOW_ID_GREEN)
        return

    def _updateEquipmentSlot(self, idx, item):
        super(BattleRoyaleConsumablesPanel, self)._updateEquipmentSlot(idx, item)
        prevQuantity = self.__quantityMap[idx]
        quantity = self.__quantityMap[idx] = item.getQuantity()
        if prevQuantity is not None and quantity > prevQuantity:
            self.as_setGlowS(idx, CONSUMABLES_PANEL_SETTINGS.GLOW_ID_GREEN)
            return
        else:
            currStage = item.getStage()
            prevStage = item.getPrevStage()
            if currStage == EQUIPMENT_STAGES.READY and prevStage == EQUIPMENT_STAGES.COOLDOWN:
                self.as_setGlowS(idx, CONSUMABLES_PANEL_SETTINGS.GLOW_ID_GREEN_SPECIAL)
            elif currStage == EQUIPMENT_STAGES.COOLDOWN and prevStage in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING, EQUIPMENT_STAGES.ACTIVE):
                self.as_setGlowS(idx, CONSUMABLES_PANEL_SETTINGS.GLOW_ID_ORANGE)
            return

    def _updateOptionalDeviceSlot(self, idx, isOn):
        pass

    def _showEquipmentGlow(self, equipmentIndex, glowType=CONSUMABLES_PANEL_SETTINGS.GLOW_ID_ORANGE):
        pass

    def __getNewSlotIdx(self, startIdx=0, endIdx=_PANEL_MAX_LENGTH - 1):
        resultIdx = None
        for idx in range(startIdx, endIdx + 1):
            if self._mask & 1 << idx == 0:
                resultIdx = idx
                break

        return resultIdx

    def __resetShellSlots(self):
        for idx in range(self._AMMO_START_IDX, self._AMMO_END_IDX + 1):
            self._mask &= ~(1 << idx)
            self._cds[idx] = None

        return

    def __onVehicleLootAction(self, state, _):
        if state != VEHICLE_VIEW_STATE.LOOT:
            return
        else:
            self.__quantityMap = [ (numItems if numItems is not None else 0) for numItems in self.__quantityMap ]
            vehStateCtrl = self.sessionProvider.shared.vehicleState
            if vehStateCtrl is not None:
                vehStateCtrl.onVehicleStateUpdated -= self.__onVehicleLootAction
            return
