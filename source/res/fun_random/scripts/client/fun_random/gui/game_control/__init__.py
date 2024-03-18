# This script contains the initialization code for Fun Random game control modules.

# Import necessary modules and classes.
from fun_random.gui.game_control.awards_controller import FunProgressionQuestsHandler  # Import the FunProgressionQuestsHandler class.
from gui.shared.system_factory import registerAwardControllerHandler  # Import the registerAwardControllerHandler function.

# Define the registerFunRandomAwardControllers function.
# This function registers the FunProgressionQuestsHandler class as an award controller handler.
def registerFunRandomAwardControllers():
    # Register the FunProgressionQuestsHandler class using the registerAwardControllerHandler function.
    registerAwardControllerHandler(FunProgressionQuestsHandler)
