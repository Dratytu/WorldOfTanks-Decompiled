# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/hangar/__init__.py

# Importing necessary modules and classes
from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from gui.Scaleform.genConsts.EPICBATTLES_ALIASES import EPICBATTLES_ALIASES
from entry_point import EpicBattlesEntryPoint

# A function that returns context menu handlers.
# Currently, this function does not contain any code, so it always returns None or an empty list.
def getContextMenuHandlers():
    pass


# A function that returns view settings.
# It returns a tuple containing a single element, which is a ComponentSettings object.
# This object specifies the EPIC_BATTLES_ENTRY_POINT component, its class (EpicBattlesEntryPoint), and the scope template (DEFAULT_SCOPE).
def getViewSettings():
    return (ComponentSettings(EPICBATTLES_ALIASES.EPIC_BATTLES_ENTRY_POINT, EpicBattlesEntryPoint, ScopeTemplates.DEFAULT_SCOPE),)


# A function that returns business handlers.
# Currently, this function does not contain any code, so it always returns None or an empty list.
def getBusinessHandlers():
    pass

