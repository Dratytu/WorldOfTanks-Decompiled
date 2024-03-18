# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/ArmoryYardPersonality.py

# Import necessary modules
from armory_yard.gui.Scaleform import registerArmoryYardScaleform, registerArmoryYardTooltipsBuilders
from armory_yard.gui.game_control import registerAYGameControllers, registerAYAwardControllers
from armory_yard.gui.shared.gui_items.items_actions import registerActions
from debug_utils import LOG_DEBUG # Import the LOG_DEBUG function for logging debug messages

# The preInit function initializes various components of the Armory Yard module
def preInit():
    # Register Scaleform components
    registerArmoryYardScaleform()
    # Register tooltip builders
    registerArmoryYardTooltipsBuilders()
    # Register game controllers
    registerAYGameControllers()
    # Register award controllers
    registerAYAwardControllers()
    # Register action handlers
    registerActions()


# The init function logs a debug message when it is called
def init():
    LOG_DEBUG('init', __name__)


# The start function does not contain any code
def start():
    pass


# The fini function does not contain any code
def fini():
    pass

