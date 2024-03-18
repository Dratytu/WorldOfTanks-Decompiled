# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_browser_overlay.py

# Import the required module for creating the BrowserInViewComponent class
from gui.Scaleform.daapi.view.lobby.event_boards.browser_in_view_component import BrowserInViewComponent

# Define the EventBoardsBrowserOverlay class, which inherits from BrowserInViewComponent
class EventBoardsBrowserOverlay(BrowserInViewComponent):
    
    # Define the setOpener method for the EventBoardsBrowserOverlay class
    def setOpener(self, view):
        # Set the URL for the browser component using the url from the view's context
        self.setUrl(view.ctx.get('url'))
        
        # Set the title for the browser component using the title from the view's context
        self.as_setTitleS(view.ctx.get('title'))

