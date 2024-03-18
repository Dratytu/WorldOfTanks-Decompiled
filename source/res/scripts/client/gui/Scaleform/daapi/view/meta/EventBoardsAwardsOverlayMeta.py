# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBoardsAwardsOverlayMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent as BaseDAAPIComponent # Importing BaseDAAPIComponent to inherit its properties and methods

class EventBoardsAwardsOverlayMeta(BaseDAAPIComponent):

    # Method to change the filter based on the given id
    def changeFilter(self, id):
        self._printOverrideError('changeFilter') # Print an error message if this method is overridden

    # Set the header data on the client side
    def as_setHeaderS(self, data):
        return self.flashObject.as_setHeader(data) if self._isDAAPIInited() else None # Return None if DAAPI is not initialized, otherwise call the method on the flashObject

    # Set the vehicle data on the client side
    def as_setVehicleS(self, data):
        return self.flashObject.as_setVehicle(data) if self._isDAAPIInited() else None # Return None if DAAPI is not initialized, otherwise call the method on the flashObject

    # Set the data on the client side
    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None # Return None if DAAPI is not initialized, otherwise call the method on the flashObject

