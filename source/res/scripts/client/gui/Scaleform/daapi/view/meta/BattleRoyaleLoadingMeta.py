# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleLoadingMeta.py

# Import the BattleLoading class from the gui.Scaleform.daapi.view.battle.shared.battle_loading module
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading

# Define the BattleRoyaleLoadingMeta class, which inherits from the BattleLoading class
class BattleRoyaleLoadingMeta(BattleLoading):

    # Define the as_setHeaderDataS method, which takes a single argument 'data'
    def as_setHeaderDataS(self, data):
        # If the DAAPI is initialized, call the as_setHeaderData method of the flashObject with 'data' as an argument
        return self.flashObject.as_setHeaderData(data) if self._isDAAPIInited() else None

