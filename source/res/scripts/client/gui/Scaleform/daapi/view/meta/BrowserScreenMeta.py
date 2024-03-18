# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserScreenMeta.py

# Import View class from gui.Scaleform.framework.entities.View, which is a metaclass for all views in the Scaleform framework
from gui.Scaleform.framework.entities.View import View

# Define BrowserScreenMeta class that inherits from View class
class BrowserScreenMeta(View):

    # Define onCloseBtnClick method, which is called when the close button is clicked
    def onCloseBtnClick(self):
        # Print an error message if this method is overridden
        self._printOverrideError('onCloseBtnClick')

    # Define onEscapePress method, which is called when the escape key is pressed
    def onEscapePress(self):
        # Print an error message if this method is overridden
        self._printOverrideError('onEscapePress')

    # Define onFocusChange method, which is called when the focus state changes
    def onFocusChange(self, hasFocus):
        # Print an error message if this method is overridden
        self._printOverrideError('onFocusChange')

    # Define viewSize method, which is called with the width and height of the view
    def viewSize(self, width, height):
        # Print an error message if this method is overridden
        self._printOverrideError('viewSize')

    # Define as_loadBrowserS method, which returns the result of as_loadBrowser() method called on the flashObject
    def as_loadBrowserS(self):
        # Only call the method if the DAAPI is initialized
        return self.flashObject.as_loadBrowser() if self._isDAAPIInited() else None

    # Define as_setBrowserParamsS method, which returns the result of as_setBrowserParams(data) method called on the flashObject
    def as_setBrowserParamsS(self, data):
        # Only call the method if the DAAPI is initialized
        return self.flashObject.as_setBrowserParams
