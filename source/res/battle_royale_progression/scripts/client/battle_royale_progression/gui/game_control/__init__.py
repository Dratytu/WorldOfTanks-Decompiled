# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/game_control/__init__.py

# Importing necessary modules and classes
# Importing BRProgressionStageHandler from the awards_controller module
from battle_royale_progression.gui.game_control.awards_controller import BRProgressionStageHandler
# Importing BRProgressionController from the progression_controller module
from battle_royale_progression.gui.game_control.progression_controller import BRProgressionController
# Importing SM_TYPE_BR_PROGRESSION from the progression_controller module
from battle_royale_progression.gui.gui_constants import SM_TYPE_BR_PROGRESSION
# Importing SYS_MESSAGE_TYPE from the chat_shared module
from chat_shared import SYS_MESSAGE_TYPE
# Importing registerAwardControllerHandler and registerGameControllers from the system_factory module
from gui.shared.system_factory import registerAwardControllerHandler, registerGameControllers
# Importing SoftException from the soft_exception module
from soft_exception import SoftException

# Function to register BR game controllers
def registerBRGameControllers():
    # Importing IBRProgressionOnTokensController from the skeletons module
    from battle_royale_progression.skeletons.game_controller import IBRProgressionOnTokensController
    
    # Registering game controllers using the registerGameControllers function
    # The function takes a list of tuples, where each tuple contains an interface class, an implementation class, and a flag indicating whether the controller is a singleton
    registerGameControllers([(IBRProgressionOnTokensController, BRProgressionController, False)])


# Function to register BR progression award controllers
def registerBRProgressionAwardControllers():
    try:
        # Checking if the attribute SM_TYPE_BR_PROGRESSION exists in SYS_MESSAGE_TYPE
        # If the attribute does not exist, an AttributeError will be raised
        SYS_MESSAGE_TYPE.__getattr__(SM_TYPE_BR_PROGRESSION).index()
    except AttributeError:
        # Raising SoftException if the attribute is not found
        raise SoftException('No index for {attr} found. Use registerSystemMessagesTypes before'.format(attr=SM_TYPE_BR_PROGRESSION))

    # Registering award controller handler using BRProgressionStageHandler
    # The function takes a handler class as an argument
    registerGameControllers([(IBRProgressionOnTokensController, BRProgressionController, False)])
