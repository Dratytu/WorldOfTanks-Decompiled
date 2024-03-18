# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/battle_hint.py

# Import the necessary modules and classes
from gui.Scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintComponent

# Define the BattleHint class, which inherits from both BattleHintComponent and BattleHintMeta
class BattleHint(BattleHintComponent, BattleHintMeta):

    # Implement the _showHint method, which takes a 'data' argument
    def _showHint(self, data):
        # Call the as_showHintS method, passing 'data' as a parameter
        self.as_showHintS(data)

    # Implement the _hideHint method
    def _hideHint(self):
        # If the 'currentHint' attribute exists:
        if self.currentHint:
            # Call the as_hideHintS method
            self.as_hideHintS()

