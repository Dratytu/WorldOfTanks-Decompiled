# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCPreBattleTimer.py

# Import necessary modules and resources
from gui.impl.gen import R  # Resource container for localization strings
from gui.impl import backport  # Helper module for backporting localization strings
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase  # Base class for pre-battle timers

# Define the BCPreBattleTimer class, which inherits from PreBattleTimerBase
class BCPreBattleTimer(PreBattleTimerBase):

    # Override the updateBattleCtx method from the base class
    def updateBattleCtx(self, battleCtx):
        # Extract the battle type string from the battle context
        self._battleTypeStr = battleCtx.getArenaWinString()
        
        # Update the message on the timer using the extracted string
        self.as_setMessageS(self._getMessage())
        
        # If the win condition should be displayed
        if self._isDisplayWinCondition():
            # Set the text for the win condition using localization string
            self.as_setWinConditionTextS(backport.text(R.strings.bootcamp.arena.name()))

    # Override the _getMessage method from the base class
    def _getMessage(self):
        # Return the battle type string
        return self._battleTypeStr

