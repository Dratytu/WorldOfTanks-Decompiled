# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/comp7/tooltips/comp7_calendar_day_extended_tooltip.py

# Import necessary modules and libraries
from datetime import datetime
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.tooltips import TOOLTIP_TYPE, formatters
from gui.Scaleform.daapi.view.lobby.comp7.tooltips.comp7_calendar_day_tooltip import Comp7CalendarDayTooltip
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock
from helpers import time_utils
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES

# Define a constant for the minimum tooltip width
_TOOLTIP_MIN_WIDTH = 210

# Subclass Comp7CalendarDayTooltip to create Comp7CalendarDayExtendedTooltip
class Comp7CalendarDayExtendedTooltip(Comp7CalendarDayTooltip):
    
    # Set the tooltip type
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_CALENDAR_DAY_EXTENDED_INFO
    
    # Override the packBlocks method to add new blocks
    def _packBlocks(self, selectedTime):
        items = []
        if self.__isSeasonEnded(selectedTime):
            return items
        blocks = []
        currentSeason = self._controller.getCurrentSeason()
        if currentSeason:
            daysLeft = int((currentSeason.getEndDate() - time_utils.getServerUTCTime()) / time_utils.ONE_DAY)
            blocks.append(self.__packTimeLeftBlock(daysLeft))
        blocks.append(self._packHeaderBlock())
        blocks.extend(self.__packCalendarBlock(selectedTime))
        items.append(formatters.packBuildUpBlockData(blocks, 13))
        return items
    
    # Pack the time left block
    def __packTimeLeftBlock(self, daysLeft):
        return formatters.packTextBlockData(text=text_styles.stats(backport.ntext(self._RES_ROOT.timeLeft(), daysLeft, days=daysLeft)), blockWidth=_TOOLTIP_MIN_WIDTH)
    
    # Check if the season has ended
    def __isSeasonEnded(self, selectedTime):
        if selectedTime is None:
            selectedTime = time_utils.getCurrentLocalServerTimestamp()
        seasonEnd = None
        if self._controller.getCurrentSeason():
            seasonEnd = self._controller.getCurrentSeason().getEndDate()
            seasonEnd = datetime.fromtimestamp(seasonEnd).date()
        return datetime.fromtimestamp(selectedTime).date() > seasonEnd
    
    # Pack the calendar block
    def __packCalendarBlock(self, selectedTime):
        return packCalendarBlock(self._controller, selectedTime, SELECTOR_BATTLE_TYPES.COMP7)

