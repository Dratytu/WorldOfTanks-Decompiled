# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventRadialMenuMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the EventRadialMenuMeta class, which inherits from BaseDAAPIComponent
class EventRadialMenuMeta(BaseDAAPIComponent):

    # Define the showHandCursor method, which prints an error message when called
    def showHandCursor(self):
        self._printOverrideError('showHandCursor')

    # Define the hideHandCursor method, which prints an error message when called
    def hideHandCursor(self):
        self._printOverrideError('hideHandCursor')

    # Define the leaveRadialMode method, which prints an error message when called
    def leaveRadialMode(self):
        self._printOverrideError('leaveRadialMode')

    # Define the as_showWithNameS method, which returns an ActionScript object
    def as_showWithNameS(self, radialState, offset, ratio, targetDisplayName):
        # Return the result of the as_showWithName method if the DAAPI is initialized, otherwise return None
        return self.flashObject.as_showWithName(radialState, offset, ratio, targetDisplayName) if self._isDAAPIInited() else None
