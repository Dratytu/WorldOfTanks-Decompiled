# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GoodieInfoMeta.py

# Import the AbstractWindowView class from the gui.Scaleform.framework.entities.abstract.AbstractWindowView module
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

# Define the GoodieInfoMeta class, which inherits from AbstractWindowView
class GoodieInfoMeta(AbstractWindowView):

    # Define the onCancelClick method, which should be overridden by a subclass
    def onCancelClick(self):
        # Print an error message if this method is called directly (since it should be overridden)
        self._printOverrideError('onCancelClick')

    # Define the as_setInfoS method, which returns the result of calling as_setInfo on the flashObject instance
    def as_setInfoS(self, data):
        # Only call as_setInfo if the DAAPI has been initialized
        return self.flashObject.as_setInfo(data) if self._isDAAPIInited() else None

