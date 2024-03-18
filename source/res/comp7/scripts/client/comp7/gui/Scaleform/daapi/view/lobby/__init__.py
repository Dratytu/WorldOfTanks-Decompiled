# Python bytecode 2.7 (decompiled from Python 2.7)

# This script is a part of the comp7 module and contains definitions for
# various components related to the lobby in the game client.

# Importing the ComponentSettings class from the gui.Scaleform.framework module,
# which is used to define the settings for a specific component.
from gui.Scaleform.framework import ComponentSettings

# Importing the ScopeTemplates class and the HANGAR_ALIASES enum from the
# gui.Scaleform.genConsts.HANGAR_ALIASES module, which are used for defining
# the scope templates and aliases for the hangar components.
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES

# The getContextMenuHandlers() function returns a pass statement, which means
# it does not contain any code to be executed. This function is likely a
# placeholder for future implementation.
def getContextMenuHandlers():
    pass

# The getViewSettings() function returns a tuple containing a single
# ComponentSettings object. This object defines the settings for the
# COMP7_MODIFIERS_PANEL component, which is injected with the Comp7ModifiersPanelInject
# class and has a default scope.
def getViewSettings():
    from comp7.gui.Scaleform.daapi.view.lobby.hangar.comp7_modifiers_panel import Comp7ModifiersPanelInject
    return (ComponentSettings(HANGAR_ALIASES.COMP7_MODIFIERS_PANEL, Comp7ModifiersPanelInject, ScopeTemplates.DEFAULT_SCOPE),)

# The getBusinessHandlers() function returns a pass statement, which means
# it does not contain any code to be executed. This function is likely a
# placeholder for future implementation.
def getBusinessHandlers():
    pass

