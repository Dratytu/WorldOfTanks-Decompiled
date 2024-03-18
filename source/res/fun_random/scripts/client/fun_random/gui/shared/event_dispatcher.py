# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/shared/event_dispatcher.py

# Import necessary modules and libraries
from frameworks.wulf import WindowLayer
from gui.impl.gen import R
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams, GuiImplViewLoadParams
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView, showModeSelectorWindow
from gui.shared.events import ModeSubSelectorEvent
from helpers import dependency
from skeletons.gui.impl import IGuiLoader

# Define the function to show the FunRandomPrimeTimeWindow
def showFunRandomPrimeTimeWindow(subModeID):
    """
    Display the FunRandomPrimeTimeWindow with the given subModeID.

    :param subModeID: The ID of the sub-mode.
    """
    ctx = {'subModeID': subModeID}
    event = events.LoadViewEvent(SFViewLoadParams(FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME), ctx=ctx)
    g_eventBus.handleEvent(event, EVENT_BUS_SCOPE.LOBBY)


# Define the function to show the FunRandomInfoPage
def showFunRandomInfoPage(infoPageUrl):
    """
    Display the FunRandomInfoPage with the given infoPageUrl.

    :param infoPageUrl: The URL of the info page.
    """
    showBrowserOverlayView(infoPageUrl, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


@dependency.replace_none_kwargs(uiLoader=IGuiLoader)
# Decorate the function with dependency injection for IGuiLoader
def showFunRandomSubSelector(uiLoader=IGuiLoader):
    """
    Display the FunRandomSubSelector.

    :param uiLoader: The IGuiLoader instance (optional, injected if not provided).
    """
    from fun_random.gui.impl.lobby.mode_selector.fun_sub_selector_view import FunModeSubSelectorView

    g_eventBus.handleEvent(ModeSubSelectorEvent(ModeSubSelectorEvent.CHANGE_VISIBILITY, ctx={'visible': True}))
    contentResId = R.views.lobby.mode_selector.ModeSelectorView()
    mainSelectorWindow = uiLoader.windowsManager.getViewByLayoutID(contentResId).getParentWindow()
    g_eventBus.handleEvent(events.LoadGuiImplViewEvent(GuiImplViewLoadParams(R.views.fun_random.lobby.feature.FunRandomModeSubSelector(), FunModeSubSelectorView, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, parent=mainSelectorWindow)), scope=EVENT_BUS_SCOPE.LOBBY)


@dependency.replace_none_kwargs(uiLoader=IGuiLoader)
# Decorate the function with dependency injection for IGuiLoader
def showFunRandomProgressionWindow(uiLoader=None):
    """
    Display the FunRandomProgressionWindow.

    :param uiLoader: The IGuiLoader instance (optional, injected if not provided).
    """
    contentResId = R.views.fun_random.lobby.feature.FunRandomProgression()
    if uiLoader.windowsManager.getViewByLayoutID(contentResId) is None:
        from fun_random.gui.impl.lobby.feature.fun_random_progression_view import FunRandomProgressionView
        params = GuiImplViewLoadParams(contentResId, FunRandomProgressionView, ScopeTemplates.LOBBY_SUB_SCOPE)
        g_eventBus.handleEvent(events.LoadGuiImplViewEvent(params), scope=EVENT_BUS_SCOPE.LOBBY)
    return


@dependency.replace_none_kwargs(uiLoader=IGuiLoader)
# Decorate the function with dependency injection for IGuiLoader
def showFunRandomModeSubSelectorWindow(uiLoader=None):
    """
    Display the FunRandomModeSubSelectorWindow.

    :param uiLoader: The IGuiLoader instance (optional, injected if not provided).
    """
    contentResId = R.views.lobby.mode_selector.ModeSelectorView()
    if uiLoader.windowsManager.getViewByLayoutID(contentResId) is
