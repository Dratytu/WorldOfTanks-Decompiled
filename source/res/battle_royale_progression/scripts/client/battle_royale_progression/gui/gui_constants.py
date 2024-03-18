# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/gui_constants.py

# Importing necessary modules and constants
from chat_shared import SYS_MESSAGE_TYPE # Importing the SYS_MESSAGE_TYPE constant from chat_shared module
from constants_utils import ConstInjector # Importing ConstInjector class from constants_utils module
from messenger import m_constants # Importing m_constants module

# Defining custom system message type for Battle Royale progression notifications
SM_TYPE_BR_PROGRESSION = 'BRProgressionNotification'

# List of system message types, including the custom Battle Royale progression notifications
_SM_TYPES = [SM_TYPE_BR_PROGRESSION]

# Defining a class SCH_CLIENT_MSG_TYPE that inherits from m_constants.SCH_CLIENT_MSG_TYPE and ConstInjector
class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    # Defining a constant BR_PROGRESSION_NOTIFICATIONS with value 300
    BR_PROGRESSION_NOTIFICATIONS = 300

# Function to register system message types
def registerSystemMessagesTypes():
    # Injecting the system message types into SYS_MESSAGE_TYPE using ConstInjector
    SYS_MESSAGE_TYPE.inject(_SM_TYPES)

