# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleTournamentWidgetMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the BattleRoyaleTournamentWidgetMeta class, which inherits from BaseDAAPIComponent
class BattleRoyaleTournamentWidgetMeta(BaseDAAPIComponent):

    # Define the as_setTitleS method, which takes a single argument 'title'
    def as_setTitleS(self, title):
        # If the DAAPI is initialized, call the as_setTitle method on the flashObject with the 'title' argument
        return self.flashObject.as_setTitle(title) if self._isDAAPIInited() else None

