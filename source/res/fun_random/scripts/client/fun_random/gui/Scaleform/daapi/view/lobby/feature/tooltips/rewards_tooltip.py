# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/rewards_tooltip.py

# Import necessary modules and classes
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression
from gui.shared.tooltips.quests import AdditionalAwardTooltipData
from fun_random.gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import FunCurtailingAwardsComposer, getFunAwardsPacker

# Set the maximum number of bonus rewards to 8
_MAX_BONUS_COUNT = 8

# Define the FunRandomRewardsTooltip class, which inherits from AdditionalAwardTooltipData and FunProgressionWatcher
class FunRandomRewardsTooltip(AdditionalAwardTooltipData, FunProgressionWatcher):

    # Decorate the _packBlocks method with @hasActiveProgression to ensure there's an active progression
    @hasActiveProgression(defReturn=[])
    # Define the _packBlocks method
    def _packBlocks(self, *args, **kwargs):
        # Initialize the formatter with the maximum bonus count and the FunAwardsPacker
        formatter = FunCurtailingAwardsComposer(_MAX_BONUS_COUNT, getFunAwardsPacker())
        # Get the formatted bonus data using the active progression's bonuses
        formattedBonuses = formatter.getShortBonusesData(self.getActiveProgression().getAllBonuses())
        # Call the parent class's _packBlocks method with the formatted bonuses as an argument
        return super(FunRandomRewardsTooltip, self)._packBlocks(*formattedBonuses)

