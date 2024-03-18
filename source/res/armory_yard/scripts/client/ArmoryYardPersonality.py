# Python 2.7.15

# Import necessary modules
from debug_utils import LOG_DEBUG

# Initialize the Armory Yard module
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


# Initialize and log a debug message
def init():
    LOG_DEBUG('init', __name__)


# No-op function
def start():
    pass


# No-op function
def fini():
    pass


# Register the initialization functions with the Armory Yard module
armory_yard_init_funcs = (preInit, init, start, fini)
