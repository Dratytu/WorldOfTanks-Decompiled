# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/messenger/formatters/__init__.py

# Import necessary modules and classes
from battle_royale_progression.gui import gui_constants
from battle_royale_progression.messenger.formatters.service_channel import BRProgressionSystemMessageFormatter
from gui.shared.system_factory import registerMessengerClientFormatter

# Define a dictionary of client formatters for different system message types
clientFormatters = {
    gui_constants.SCH_CLIENT_MSG_TYPE.BR_PROGRESSION_NOTIFICATIONS: BRProgressionSystemMessageFormatter()
}

# Function to register the client formatters with the messenger system
def registerMessengerClientFormatters():
    for sysMsgType, formatter in clientFormatters.iteritems():
        registerMessengerClientFormatter(sysMsgType, formatter)
