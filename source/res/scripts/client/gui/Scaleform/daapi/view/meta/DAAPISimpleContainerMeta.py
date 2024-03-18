# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DAAPISimpleContainerMeta.py

# Import the BaseDAAPIModule class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

# Define the DAAPISimpleContainerMeta class, which inherits from BaseDAAPIModule
class DAAPISimpleContainerMeta(BaseDAAPIModule):

    # as_populateS() method: Sends the "populate" event to the client-side
    def as_populateS(self):
        # If the DAAPI is initialized, call the "populate" method on the flashObject
        return self.flashObject.as_populate() if self._isDAAPIInited() else None

    # as_disposeS() method: Sends the "dispose" event to the client-side
    def as_disposeS(self):
        # If the DAAPI is initialized, call the "dispose" method on the flashObject
        return self.flashObject.as_dispose() if self._isDAAPIInited() else None

