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
        """
        This method is called when a user clicks on a style in the ranked battles rewards leagues view.
        The `styleID` parameter is the unique identifier for the style that was clicked.
        If this method is overridden, an error message will be printed to the console.
        """

    # as_setRewardsS method is defined to set rewards
    def as_setRewardsS(self, rewards):
        # Return the result of as_setRewards if DAAPI is initialized, otherwise return None
        return self.flashObject.as_setRewards(rewards) if self._isDAAPIInited() else None
        """
        This method is used to set the rewards for the ranked battles rewards leagues view.
        The `rewards` parameter is a data structure containing information about the rewards.
        The method returns the result of the `as_setRewards` method if DAAPI is initialized,
        otherwise it returns None.
        """
