# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: abc_tester/scripts/client/AbcTesterPersonality.py

# Import necessary modules for debugging and logging purposes.
from debug_utils import LOG_DEBUG

# Define a tuple of extension packages for the lobby.
LOBBY_EXT_PACKAGES = ()

# Define a tuple of extension packages for the battle.
BATTLE_EXT_PACKAGES = ()

# The 'preInit' function is called before the initialization process.
# It logs a debug message indicating the start of the personality initialization.
def preInit():
    LOG_DEBUG('preInit personality:', __name__)

# The 'init' function is called during the initialization process.
# In this case, it does not contain any specific initialization logic.
def init():
    pass

# The 'start' function is called when the personality is ready to start.
# In this case, it does not contain any specific start-up logic.
def start():
    pass

# The 'fini' function is called when the personality is being shut down.
# In this case, it does not contain any specific cleanup logic.
def fini():

