# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/calendar_day_tooltip.py

# Import necessary modules and libraries
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.shared.tooltips import TooltipType
from gui.impl.gen import R
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip
from helpers.time_utils import ONE_DAY

# Define the FunRandomCalendarDayTooltip class, which inherits from PeriodicCalendarDayTooltip and FunSubModesWatcher
class FunRandomCalendarDayTooltip(PeriodicCalendarDayTooltip, FunSubModesWatcher):
    # Set the tooltip type as a class variable
    _TOOLTIP_TYPE = TooltipType.FUN_RANDOM
    # Set the resource root for this tooltip
    _RES_ROOT = R.strings.fun_random.calendarDay


