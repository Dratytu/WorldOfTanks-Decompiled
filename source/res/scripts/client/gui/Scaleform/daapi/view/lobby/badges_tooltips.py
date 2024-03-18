# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/badges_tooltips.py

# Import necessary modules and constants
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.formatters import text_styles, icons
from gui.shared.tooltips import formatters
from gui.shared.tooltips.common import BlocksTooltipData

# Define the minimum width for the tooltip
_TOOLTIP_MIN_WIDTH = 362

# Define the BadgesSuffixItem class, which inherits from BlocksTooltipData
class BadgesSuffixItem(BlocksTooltipData):

    # Initialize the class with the context
    def __init__(self, context):
        super(BadgesSuffixItem, self).__init__(context, TOOLTIPS_CONSTANTS.BADGES_SUFFIX_ITEM)
        self._setContentMargin(top=15, left=20, bottom=10, right=15)
        self._setMargins(afterBlock=0)
        self._setWidth(_TOOLTIP_MIN_WIDTH)

    # Pack the blocks for the tooltip
    def _packBlocks(self, *args, **kwargs):
        self._badgeId = args[0]
        return [formatters.packBuildUpBlockData([self.packHeader(), self.packBody()], gap=-2)]

    # Pack the header block for the tooltip
    def packHeader(self):
        title = text_styles.middleTitle(backport.text(R.strings.badge.dyn('badge_{}'.format(self._badgeId))()))
        icon = backport.image(R.images.gui.maps.icons.library.badges.c_24x24.dyn('badge_{}'.format(self._badgeId))())
        value = icons.makeImageTag(backport.image(R.images.gui.maps.icons.library.badges.strips.c_64x24.dyn('strip_{}'.format(self._badgeId))()), 64, 24)
        return formatters.packTitleDescParameterWithIconBlockData(title=title, icon=icon, value=value, iconPadding=formatters.packPadding(left=3), valuePadding=formatters.packPadding(left=-80, top=-2), valueAtRight=True)

    # Pack the body block for the tooltip
    def packBody(self):
        return formatters.packTextBlockData(text_styles.main(backport.text(R.strings.badge.dyn('badge_{}_descr'.format(self._badgeId))())))


# Define the BadgesSuffixRankedItem class, which inherits from BadgesSuffixItem
class BadgesSuffixRankedItem(BadgesSuffixItem):

    # Pack the body block for the tooltip
    def packBody(self):
        items = [formatters.packTextBlockData(text_styles.main(backport.text(R.strings.tooltips.badgepage.ranked.suffixItem.position())), padding=formatters
