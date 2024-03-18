# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/Scaleform/__init__.py

# Importing the 'genConsts.TOOLTIPS_CONSTANTS' module from 'gui.Scaleform'
from gui.Scaleform.genConsts import TOOLTIPS_CONSTANTS

# Importing the 'registerScaleformLobbyPackages' and 'registerLobbyTooltipsBuilders' functions
# from 'gui.shared.system_factory'
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders

# This function registers the Scaleform packages for the Armory Yard lobby
def registerArmoryYardScaleform():
    # The 'registerScaleformLobbyPackages' function takes a tuple of package names as an argument
    # Here, it registers the 'armory_yard.gui.Scaleform.daapi.view.lobby' package
    registerScaleformLobbyPackages(('armory_yard.gui.Scaleform.daapi.view.lobby',))


# This function registers the tooltip builders for the Armory Yard lobby
def registerArmoryYardTooltipsBuilders():
    # The 'registerLobbyTooltipsBuilders' function takes a list of tooltip builder configurations as an argument
    # Here, it registers the 'armory_yard.gui.Scaleform.daapi.view.tooltips.lobby_builders' package
    # with the tooltip set 'TOOLTIPS_CONSTANTS.ARMORY_YARD_LOBBY_SET'
    registerLobbyTooltipsBuilders([('armory_yard.gui.Scaleform.daapi.view.tooltips.lobby_builders', TOOLTIPS_CONSTANTS.ARMORY_YARD_LOBBY_SET)])

