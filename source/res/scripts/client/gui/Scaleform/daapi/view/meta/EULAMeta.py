# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EULAMeta.py

# Import the AbstractWindowView class from the gui.Scaleform.framework.entities.abstract package
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

# Define the EULAMeta class, which inherits from AbstractWindowView
class EULAMeta(AbstractWindowView):

    # Define the requestEULAText method, which prints an error message when called
    def requestEULAText(self):
        self._printOverrideError('requestEULAText')

    # Define the onLinkClick method, which prints an error message when called
    def onLinkClick(self, url):
        self._printOverrideError('onLinkClick')

    # Define the onApply method, which prints an error message when called
    def onApply(self):
        self._printOverrideError('onApply')

    # Define the as_setEULATextS method, which returns the result of calling the as_setEULAText method on the flashObject attribute
    def as_setEULATextS(self, text):
        return self.flashObject.as_setEULAText(text) if self._isDAAPIInited() else None

