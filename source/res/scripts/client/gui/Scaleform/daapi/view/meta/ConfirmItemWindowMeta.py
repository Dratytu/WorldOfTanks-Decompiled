# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmItemWindowMeta.py

# Import the AbstractWindowView class from the gui.Scaleform.framework.entities.abstract.AbstractWindowView module.
# This class is the base class for all window views in the Scaleform framework.
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

# Define the ConfirmItemWindowMeta class, which inherits from AbstractWindowView.
class ConfirmItemWindowMeta(AbstractWindowView):

    # The submit method is called when the user confirms the action in the window.
    # It takes two arguments: count and currency.
    def submit(self, count, currency):
        # Print an error message if the method is overridden.
        self._printOverrideError('submit')

    # The as_setDataS method is used to set data on the client side.
    # It takes one argument: value.
    def as_setDataS(self, value):
        # Return the result of calling the as_setData method on the flashObject if the DAAPI is initialized.
        return self.flashObject.as_setData(value) if self._isDAAPIInited() else None

    # The as_setSettingsS method is used to set settings on the client side.
    # It takes one argument: value.
    def as_setSettingsS(self, value):
        # Return the result of calling the as_setSettings method on the flashObject if the DAAPI is initialized.
        return self.flashObject.as_setSettings(value) if self._isDAAPIInited() else None
