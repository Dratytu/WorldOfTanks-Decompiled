# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/BrowserWindow.py

# Import necessary modules and libraries
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BrowserWindowMeta import BrowserWindowMeta
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import event_bus_handlers, events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.game_control import IBrowserController

# Define the BrowserWindow class, inheriting from BrowserWindowMeta
class BrowserWindow(BrowserWindowMeta):
    # Declare dependency on IBrowserController
    browserCtrl = dependency.descriptor(IBrowserController)

    # Class constructor
    def __init__(self, ctx=None):
        super(BrowserWindow, self).__init__()
        # Initialize class variables with values from ctx dictionary
        self.__size = ctx.get('size')
        self.__browserID = ctx.get('browserID')
        self.__customTitle = ctx.get('title')
        self.__showActionBtn = ctx.get('showActionBtn', True)
        self.__showWaiting = ctx.get('showWaiting', False)
        self.__showCloseBtn = ctx.get('showCloseBtn', False)
        self.__isSolidBorder = ctx.get('isSolidBorder', False)
        self.__alias = ctx.get('alias', '')
        self.__handlers = ctx.get('handlers', None)

    # onRegisterFlashComponent event handler
    def _onRegisterFlashComponent(self, viewPy, alias):
        super(BrowserWindow, self)._onRegisterFlashComponent(viewPy, alias)
        # Initialize the web browser with the given browserID, handlers, and alias
        if alias == VIEW_ALIAS.BROWSER:
            viewPy.init(self.__browserID, self.__handlers, self.__alias)

    # onWindowClose event handler
    def onWindowClose(self):
        webBrowser = self.browserCtrl.getBrowser(self.__browserID)
        if webBrowser is not None:
            webBrowser.onUserRequestToClose()
        else:
            LOG_ERROR('Browser not found. Browser id = "{}"'.format(self.__browserID))
        self.destroy()

    # _populate method, called when the window is displayed
    def _populate(self):
        super(BrowserWindow, self)._populate()
        # Configure the window with the given title, showActionBtn, showCloseBtn, and isSolidBorder
        self.as_configureS(self.__customTitle, self.__showActionBtn, self.__showCloseBtn, self.__isSolidBorder)
        # Set the window size
        self.as_setSizeS(*self.__size)
        if self.__showWaiting:
            # Display a waiting message
            self.as_showWaitingS(backport.msgid(R.strings.waiting.loadContent()), {})

    # eventBusHandler for HideWindowEvent.HIDE_BROWSER_WINDOW
    @event_bus_handlers.eventBusHandler(events.HideWindowEvent.HIDE_BROWSER_WINDOW, EVENT_BUS_SCOPE.LOBBY)
    def __handleBrowserClose(self, event):
        if event.ctx.get('browserID') == self.__browserID:
            self.destroy()
