# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/__init__.py

# Import necessary modules and constants
from constants import ARENA_GUI_TYPE
from gui.Scaleform.daapi.settings import config as sf_config
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders, registerScaleformBattlePackages

# Define a function to register the necessary Scaleform packages and tooltips for the fun_random module
def registerFunRandomScaleform():
    # Register the lobby packages for the fun_random module
    registerScaleformLobbyPackages(('fun_random.gui.Scaleform.daapi.view.lobby',))
    
    # Register the battle packages for the fun_random module
    registerScaleformBattlePackages(ARENA_GUI_TYPE.FUN_RANDOM, sf_config.BATTLE_PACKAGES + ('fun_random.gui.Scaleform.daapi.view.battle',))
    
    # Register the lobby tooltips builders for the fun_random module
    registerLobbyTooltipsBuilders([('fun_random.gui.Scaleform.daapi.view.tooltips.lobby_builders', _TOOLTIPS.FUN_RANDOM_LOBBY_SET)])
