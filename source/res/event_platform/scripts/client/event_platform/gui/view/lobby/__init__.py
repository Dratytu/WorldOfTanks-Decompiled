# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: event_platform/scripts/client/event_platform/gui/view/lobby/__init__.py

# Import necessary modules and classes
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.bootcamp import BCHangar
from gui.Scaleform.daapi.view.bootcamp.bootcamp_cm_handlers import BCVehicleContextMenuHandler
from gui.Scaleform.daapi.view.bootcamp.component_override import BootcampComponentOverride
from gui.Scaleform.framework import ScopeTemplates, ConditionalViewSettings
from event_platform.gui.impl.event_hangar import EventHangar
from event_platform.gui.impl.lobby_cm import EPVehicleContextMenuHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE

# This function returns a tuple of context menu handlers for the lobby
def getContextMenuHandlers():
    # The tuple contains a single tuple, which maps a context menu type (VEHICLE)
    # to a BootcampComponentOverride instance. This instance combines an EventHangar
    # context menu handler (EPVehicleContextMenuHandler) and a bootcamp context menu handler
    # (BCVehicleContextMenuHandler).
    return ((CONTEXT_MENU_HANDLER_TYPE.VEHICLE, BootcampComponentOverride(EPVehicleContextMenuHandler, BCVehicleContextMenuHandler)),)


# This function returns a tuple of view settings for the lobby
def getViewSettings():
    # The tuple contains a single ConditionalViewSettings instance.
    # This instance specifies the view alias (LOBBY_HANGAR), the main view class (EventHangar),
    # the SWF file to load ('hangar.swf'), the window layer (SUB_VIEW),
    # the parent scope (None), and
