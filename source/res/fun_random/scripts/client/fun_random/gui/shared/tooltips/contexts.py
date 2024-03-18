# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/shared/tooltips/contexts.py

# Import necessary modules and constants
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from constants import ARENA_BONUS_TYPE
from gui.shared.tooltips.contexts import CarouselContext
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

# Define a new class FunRandomCarouselContext that inherits from CarouselContext
class FunRandomCarouselContext(CarouselContext):
    # Inject the ILobbyContext dependency
    __lobbyContext = dependency.descriptor(ILobbyContext)

    # Override the getStatsConfiguration method
    def getStatsConfiguration(self, item):
        # Call the superclass method to get the base stats configuration
        value = super(FunRandomCarouselContext, self).getStatsConfiguration(item)

        # Get the CrystalRewardConfig from the lobby context
        config = self.__lobbyContext.getServerSettings().getCrystalRewardConfig()

        # Set the showEarnCrystals attribute in the stats configuration
        value.showEarnCrystals = config.isCrystalEarnPossible(ARENA_BONUS_TYPE.FUN_RANDOM)

        # Check if the FUN_RANDOM bonus type has any of the daily multiplied XP caps
        value.dailyXP = ARENA_BONUS_TYPE_CAPS.checkAny(ARENA_BONUS_TYPE.FUN_RANDOM, ARENA_BONUS_TYPE_CAPS.DAILY_MULTIPLIED_XP)

        # Return the updated stats configuration
        return value

