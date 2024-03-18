# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleHintMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities module
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the BattleHintMeta class, which inherits from BaseDAAPIComponent
class BattleHintMeta(BaseDAAPIComponent):

    # Define the as_showHintS method, which takes a single argument 'data'
    def as_showHintS(self, data):
        # If the DAAPI is initialized, call the as_showHint method on the flashObject with 'data' as the argument
        return self.flashObject.as_showHint(data) if self._isDAAPIInited() else None

    # Define the as_hideHintS method, which does not take any arguments
    def as_hideHintS(self):
        # If the DAAPI is initialized, call the as_hideHint method on the flashObject
        return self.flashObject.as_hideHint() if self._isDAAPIInited() else None

