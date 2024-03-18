# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/game_control/__init__.py

# Importing necessary modules and classes
from battle_royale_progression.gui.game_control.awards_controller import BRProgressionStageHandler
from battle_royale_progression.gui.game_control.progression_controller import BRProgressionController
from battle_royale_progression.gui.gui_constants import SM_TYPE_BR_PROGRESSION
from chat_shared import SYS_MESSAGE_TYPE
from gui.shared.system_factory import registerAwardControllerHandler, registerGameControllers
from soft_exception import SoftException

# Function to register BR game controllers
def registerBRGameControllers():
    # Importing IBRProgressionOnTokensController from the skeletons module
    from battle_royale_progression.skeletons.game_controller import IBRProgressionOnTokensController
    
    # Registering game controllers using the registerGameControllers function
    registerGameControllers([(IBRProgressionOnTokensController, BRProgressionController, False)])


# Function to register BR progression award controllers
def registerBRProgressionAwardControllers():
    try:
        # Checking if the attribute exists in SYS_MESSAGE_TYPE
        SYS_MESSAGE_TYPE.__getattr__(SM_TYPE_BR_PROGRESSION).index()
    except AttributeError:
        # Raising SoftException if the attribute is not found
        raise SoftException('No index for {attr} found. Use registerSystemMessagesTypes before'.format(attr=SM_TYPE_BR_PROGRESSION))

    # Registering award controller handler using BRProgressionStageHandler
    registerAwardControllerHandler(BRProgressionStageHandler)
