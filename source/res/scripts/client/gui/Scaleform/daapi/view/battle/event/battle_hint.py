# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/battle_hint.py
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintComponent
from gui.Scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta

class BattleHint(BattleHintComponent, BattleHintMeta):

    def _showHint(self, hint, data):
        hintName = hint.name
        vo = hint.makeVO(data)
        self.as_showHintS(hintName, vo)

    def _hideHint(self):
        self.as_hideHintS()

    def _finishHint(self):
        self.as_closeHintS()
