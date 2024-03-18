# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/fun_gui_constants.py

# Import necessary modules
from constants_utils import ConstInjector
from gui.prb_control import settings  # Importing settings from prb_control
from messenger import m_constants  # Importing m_constants from messenger

# Define a constant string for the attribute name
ATTR_NAME = 'FUN_RANDOM'

# Define a constant integer for the prb request type attribute name
PRB_REQ_TYPE_ATTR_NAME = 'CHANGE_FUN_SUB_MODE'

# Inherit from FUNCTIONAL_FLAG and ConstInjector
class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    # Define a constant integer for FUN_RANDOM
    FUN_RANDOM = 268435456

# Inherit from PREBATTLE_ACTION_NAME and ConstInjector
class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    # Define a constant string for FUN_RANDOM
    _const_type = str
    FUN_RANDOM = 'fun_random'
    # Define a constant string for FUN_RANDOM_SQUAD
    FUN_RANDOM_SQUAD = 'funRandomSquad'

# Inherit from SELECTOR_BATTLE_TYPES and ConstInjector
class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    # Define a constant string for FUN_RANDOM
    _const_type = str
    FUN_RANDOM = 'funRandom'

# Inherit from REQUEST_TYPE and ConstInjector
class REQUEST_TYPE(settings.REQUEST_TYPE, ConstInjector):
    # Define a constant integer for CHANGE_FUN_SUB_MODE
    CHANGE_FUN_SUB_MODE = 47

# Inherit from SCH_CLIENT_MSG
