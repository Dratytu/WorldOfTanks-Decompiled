# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationListButtonMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities module
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the NotificationListButtonMeta class, which inherits from BaseDAAPIComponent
class NotificationListButtonMeta(BaseDAAPIComponent):

    # Define the handleClick method, which is called when the button is clicked
    def handleClick(self):
        # Print an error message indicating that handleClick is overridden but not implemented
        self._printOverrideError('handleClick')

    # Define the as_setStateS method, which is used to set the state of the button
    def as_setStateS(self, isBlinking, counterValue):
        # If the DAAPI is initialized, call the as_setState method on the flashObject
        return self.flashObject.as_setState(isBlinking, counterValue) if self._isDAAPIInited() else None

