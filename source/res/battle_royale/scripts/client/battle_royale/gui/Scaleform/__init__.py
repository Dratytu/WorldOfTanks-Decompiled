# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/__init__.py

# Import necessary modules and constants
from gui.shared.system_factory import register_scaleform_battle_packages, register_scaleform_lobby_packages, register_battle_tooltips_builders, register_lobby_tooltips_builders
from constants import ARENA_GUI_TYPE
from gui.Scaleform.daapi.settings import config as sf_config
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS

# Define a function to register battle royale battle packages
def register_battle_royale_battle_packages():
    """
    Registers the scaleform battle packages for the battle royale arena GUI type.
    :return: None
    """
    register_scaleform_battle_packages(ARENA_GUI_TYPE.BATTLE_ROYALE, sf_config.BATTLE_PACKAGES + ('battle_royale.gui.Scaleform.daapi.view.battle',))

# Define a function to register battle royale lobby packages
def register_battle_royale_lobby_packages():
    """
    Registers the scaleform lobby packages for the battle royale GUI type.
    :return: None
    """
    register_scaleform_lobby_packages(['battle_royale.gui.Scaleform.daapi.view.lobby'])

# Define a function to register battle royale tooltip builders
def register_battle_royale_tooltips_builders():
    """
    Registers the battle royale tooltip builders for the battle and lobby GUI types.
    :return: None
    """
    register_battle_tooltips_builders([('battle_royale.gui.Scaleform.da
