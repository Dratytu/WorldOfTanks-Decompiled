# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_progression_tooltip.py

import logging
import string
from gui.impl.gen import R
from gui.impl import backport
from gui.Scaleform.genConsts.PROGRESSCOLOR_CONSTANTS import PROGRESSCOLOR_CONSTANTS
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.daapi.view.lobby.mapbox import mapbox_helpers
from gui.shared.formatters import text_styles
from gui.shared.tooltips import formatters, TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

# Logger for this module
_logger = logging.getLogger(__name__)

# Image path constants
_IMG_PATH = R.images.gui.maps.icons.mapbox

# String path constants
_STR_PATH = R.strings.mapbox.questFlag

# Number of maps in a row
_MAPS_IN_ROW = 3

# Maximum number of maps in a row
_MAX_MAPS_IN_ROW = 4

# Name mapping for maps
_NAME_MAPPING = {'all': 'all'}

class MapboxProgressionTooltip(BlocksTooltipData):
    """
    Class for creating a tooltip for Mapbox progression.
    """
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    def __init__(self, context):
        """
        Initialize the MapboxProgressionTooltip instance.

        :param context: The context of the tooltip.
        """
        super(MapboxProgressionTooltip, self).__init__(context, TOOLTIP_TYPE.MAPBOX_SELECTOR_INFO)
        self._setWidth(350)  # Set the width of the tooltip
        self._setContentMargin(top=0, left=0, bottom=16, right=0)  # Set the content margin

    def _packBlocks(self, *args):
        """
        Pack the blocks for the tooltip.

        :return: A list of packed blocks.
        """
        items = []
        progressionData = self.__mapboxCtrl.getProgressionData()  # Get the progression data
        if progressionData is not None and self.__mapboxCtrl.isActive():
            items.append(self.__packHeaderBlock())  # Add the header block
            items.append(self.__packDescriptionBlock())  # Add the description block
            items.append(self.__packTotalProgressionBlock(progressionData))  # Add the total progression block
            items.append(self.__packMapsProgressionBlock(progressionData))  # Add the maps progression block
        else:
            items.append(self.__packFrozenBlock())  # Add the frozen block
        return items  # Return the packed blocks

    def __packHeaderBlock(self):
        """
        Pack the header block.

        :return: The packed header block.
        """
        header = backport.text(R.strings.tooltips.battleTypes.mapbox.header())
        timeLeftStr = text_styles.stats(mapbox_helpers.getTillTimeString(self.__mapboxCtrl.getEventEndTimestamp()))
        body = backport.text(R.strings.menu.headerButtons.battle.types.mapbox.extra.endsIn(), timeLeft=timeLeftStr)
        return formatters.packImageTextBlockData(title=text_styles.highTitle(header), desc=text_styles.main(body), img=backport.image(_IMG_PATH.quests.tooltip_header_bg()), txtOffset=1, txtPadding=formatters.packPadding(top=15, left=17), padding=formatters.packPadding(bottom=-10))

    def __packDescriptionBlock(self):
        """
        Pack the description block.

        :return: The packed description block.
        """
        return formatters.packTextBlockData(text_styles.main(backport.text(_STR_PATH.description(), highlightedText=text_styles.stats(backport.text(_STR_PATH.highlightedText())))), padding=formatters.packPadding(left=18, right=10))

    def __packTotalProgressionBlock(self, progressionData):
        """
        Pack the total progression block.

        :param progressionData: The progression data.
        :return: The packed total progression block.
        """
        progress = progressionData.totalBattles
        total = max(progressionData.rewards)
        items = []
        progressStyle = text_styles.bonusAppliedText if progress >= total else text_styles.bonusPreviewText
        progressionCounter = [formatters.packTextBlockData(text_styles.stats(backport.text(_STR_PATH.progressTitle())), blockWidth=250, padding=formatters.packPadding(left=18)), formatters.packAlignedTextBlockData(backport.text(_STR_PATH.counter(), progress=progressStyle(min(progress, total)), total=text_styles.main(total)), blockWidth=85, align=BLOCKS_TOOLTIP_TYPES.ALIGN_RIGHT)]
        items.append(formatters.packBuildUpBlockData(progressionCounter, layout=BLOCKS_TOOLTIP_TYPES.LAYOUT_HORIZONTAL))
        progressColor = PROGRESSCOLOR_CONSTANTS.GREEN if progress >= total else PROGRESSCOLOR_CONSTANTS.ORANGE
        items.append(formatters.packBlockDataItem(linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_EPIC_PROGRESS_BLOCK_LINKAGE, data={'value': min(progress, total),
                                                                                                                   'maxValue': total,
                                                                                                                   'progressColor': progressColor
