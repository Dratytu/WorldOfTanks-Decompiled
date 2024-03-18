# This script contains the implementation for the battle royale progression messenger formatters.

# Import necessary modules and classes
from battle_royale_progression.gui import gui_constants  # Import the gui_constants module from the battle_royale_progression.gui package
from battle_royale_progression.messenger.formatters.service_channel import BRProgressionSystemMessageFormatter  # Import the BRProgressionSystemMessageFormatter class from the battle_royale_progression.messenger.formatters.service_channel module
from gui.shared.system_factory import registerMessengerClientFormatter  # Import the registerMessengerClientFormatter function from the gui.shared.system_factory module

# Define a dictionary of client formatters for different system message types
clientFormatters = {
    gui_constants.SCH_CLIENT_MSG_TYPE.BR_PROGRESSION_NOTIFICATIONS: BRProgressionSystemMessageFormatter()
}
# The clientFormatters dictionary maps different system message types to their corresponding formatter objects.
# In this case, the BR_PROGRESSION_NOTIFICATIONS message type is mapped to an instance of BRProgressionSystemMessageFormatter.

# Function to register the client formatters with the messenger system
def registerMessengerClientFormatters():
    for sysMsgType, formatter in clientFormatters.iteritems():
        registerMessengerClientFormatter(sysMsgType, formatter)
# The registerMessengerClientFormatters function registers the client formatters with the messenger system.
# It iterates over each system message type and formatter in the clientFormatters dictionary and calls the registerMessengerClientFormatter function
# to register each formatter with the corresponding system message type.
