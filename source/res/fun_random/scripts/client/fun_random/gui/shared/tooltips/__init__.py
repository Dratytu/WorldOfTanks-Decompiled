# This module defines a container class for tooltip types used in the fun_random module.
# The tooltip types are used to differentiate between different kinds of tooltips in the
# user interface.

from shared_utils import CONST_CONTAINER  # Importing the CONST_CONTAINER class from shared_utils module.

class TooltipType(CONST_CONTAINER):
    # TooltipType is a subclass of CONST_CONTAINER, which is used to define a set of named
    # constants for tooltip types. This allows for easier and more readable code when
    # referencing tooltip types throughout the module.

    FUN_RANDOM = 'funRandom'
    # The 'FUN_RANDOM' constant is defined as a string with the value 'funRandom'. This
    # constant represents the tooltip type for fun_random related tooltips.
