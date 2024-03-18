# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicRandomPlayersPanelMeta.py

# Importing the PlayersPanel class from the gui.Scaleform.daapi.view.battle.classic.players_panel module
from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

# Defining the EpicRandomPlayersPanelMeta class that inherits from the PlayersPanel class
class EpicRandomPlayersPanelMeta(PlayersPanel):

    # Defining the focusedColumnChanged method that overrides the same method in the PlayersPanel class
    def focusedColumnChanged(self, value):
        # Printing an error message indicating that the method is overridden and should not be called
        self._printOverrideError('focusedColumnChanged')

    # Defining the as_setPlayersSwitchingAllowedS method that is specific to the EpicRandomPlayersPanelMeta class
    def as_setPlayersSwitchingAllowedS(self, isAllowed):
        # Calling the as_setPlayersSwitchingAllowed method of the flashObject if the daapi is initialized
        return self.flashObject.as_setPlayersSwitchingAllowed(isAllowed) if self._isDAAPIInited() else None

