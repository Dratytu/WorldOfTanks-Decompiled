# This script contains definitions and registrations for server events related to the "fun random" feature.

# Import the FunProgressionTriggerQuestBuilder class, which is used to build quests related to the "fun random" feature.
from fun_random.gui.server_events.event_items import FunProgressionTriggerQuestBuilder

# Use the registerQuestBuilder function from the gui.shared.system_factory module to register the FunProgressionTriggerQuestBuilder.
# This allows the game to use the FunProgressionTriggerQuestBuilder to build quests related to the "fun random" feature.
from gui.shared.system_factory import registerQuestBuilder

# Define a function to register all "fun random" quests with the game.
def registerFunRandomQuests():
    # Register the FunProgressionTriggerQuestBuilder with the game using the registerQuestBuilder function.
    # This allows the game to use the FunProgressionTriggerQuestBuilder to build quests related to the "fun random" feature.
    registerQuestBuilder(FunProgressionTriggerQuestBuilder)
