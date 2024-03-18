# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/common/filter_popover.py

# Import necessary modules and constants
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import ARENA_BONUS_TYPE
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from gui.Scaleform.daapi.view.common.filter_popover import FILTER_SECTION, BattlePassCarouselFilterPopover
from gui.impl import backport
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

# Define a helper function to fill the FunRandom filter Visual Object (VO)
def fillFunRandomFilterVO(vo, selected, enabled):
    # Update the vo with necessary properties
    vo.update({
        'value': backport.image(FunAssetPacksMixin.getModeIconsResRoot().library.carousel_filter()),
        'tooltip': makeTooltip(header=backport.text(FunAssetPacksMixin.getModeLocalsResRoot().tooltip.filter.header()), body=backport.text(FunAssetPacksMixin.getModeLocalsResRoot().tooltip.filter.body())),
        'selected': selected,
        'enabled': enabled
    })
    return vo

# Subclass BattlePassCarouselFilterPopover to create a custom filter popover for FunRandom
class FunRandomCarouselFilterPopover(BattlePassCarouselFilterPopover):
    # Declare dependency on ILobbyContext
    __lobbyContext = dependency.descriptor(ILobbyContext)

    # Override the class method _generateMapping to customize the filter mapping
    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, **kwargs):
        # Call the superclass method to get the original mapping
        mapping = super(FunRandomCarouselFilterPopover, cls)._generateMapping(hasRented, hasEvent, hasRoles, **kwargs)

        # Modify the 'SPECIALS' section of the mapping
        filterSpecialsList = mapping[FILTER_SECTION.SPECIALS]
        filterSpecialsList.append('funRandom')
        if 'clanRented' in filterSpecialsList:
            filterSpecialsList.remove('clanRented')

        # Configure filterSpecialsList based on server settings
        config = cls.__lobbyContext.getServerSettings().getCrystalRewardConfig()
        if not config.isCrystalEarnPossible(ARENA_BONUS_TYPE.FUN_RANDOM):
            filterSpecialsList.remove('crystals')
        if not BONUS_CAPS.checkAny(ARENA_BONUS_TYPE.FUN_RANDOM, BONUS_CAPS.DAILY_MULTIPLIED_XP):
            filterSpecialsList.remove('bonus')

        # Return the modified mapping
        return mapping

    # Override the _packSpecial method to customize the packing of the 'funRandom' filter
    def _packSpecial(self, entry, ctx, selected, tooltipRes, enabled):
        # If the entry is not 'funRandom', call the superclass method
        if entry != 'funRandom':
            return super(FunRandomCarouselFilterPopover, self)._packSpecial(entry, ctx, selected, tooltipRes, enabled)
        # Otherwise, use the helper function to fill the FunRandom filter VO
        return fillFunRandomFilter
