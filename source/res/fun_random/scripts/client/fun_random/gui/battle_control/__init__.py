# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/__init__.py

# Importing necessary modules and constants
from constants import ARENA_GUI_TYPE
from fun_random.gui.ingame_help.fun_random_pages import FunRandomHelpPagesBuilder
from fun_random.helpers.tips import FunRandomTipsCriteria
from gui.shared.system_factory import registerBattleTipCriteria, registerIngameHelpPagesBuilder

# Define a function to register FunRandom-specific battle components
def registerFunRandomBattle():
    # Register a custom battle tip criteria for FunRandom arenas
    registerBattleTipCriteria(ARENA_GUI_TYPE.FUN_RANDOM, FunRandomTipsCriteria)
    
    # Register a builder function for FunRandom ingame help pages
    registerIngameHelpPagesBuilder(FunRandomHelpPagesBuilder)
