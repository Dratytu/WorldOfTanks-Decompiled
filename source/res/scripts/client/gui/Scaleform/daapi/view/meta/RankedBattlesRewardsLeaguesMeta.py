# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesRewardsLeaguesMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the RankedBattlesRewardsLeaguesMeta class, which inherits from BaseDAAPIComponent
class RankedBattlesRewardsLeaguesMeta(BaseDAAPIComponent):

    # onStyleClick method is defined to handle a user clicking on a style
    def onStyleClick(self, styleID):
        # Print an error message if onStyleClick is overridden
        self._printOverrideError('onStyleClick')

    # as_setRewardsS method is defined to set rewards
    def as_setRewardsS(self, rewards):
        # Return the result of as_setRewards if DAAPI is initialized, otherwise return None
        return self.flashObject.as_setRewards(rewards) if self._isDAAPIInited() else None
