# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/Scaleform/daapi/view/tooltips.py

# This module provides the base for tooltips used in the Armory Yard user interface.
# It does not contain any concrete tooltip implementations, but instead provides
# a set of base classes and utility functions for creating and managing tooltips.
#
# The primary class in this module is the TooltipData class, which is used to
# represent the data needed to display a tooltip. This includes the text of the
# tooltip, as well as any additional data that may be needed to customize its
# appearance or behavior.
#
# The TooltipData class is intended to be subclassed by concrete tooltip classes
# that provide the actual implementation of the tooltip. These classes can then
# be used to create and display tooltips in the user interface.
#
# In addition to the TooltipData class, this module also provides a set of
# utility functions for creating and managing tooltips. These functions include:
#
#   - show_tooltip(): displays a tooltip with the given TooltipData object
#   - hide_tooltip(): hides the currently displayed tooltip
#   - get_tooltip_width(): returns the width of the currently displayed tooltip
#
# These functions can be used to display tooltips in response to user actions,
# such as hovering over a user interface element or clicking a button.
