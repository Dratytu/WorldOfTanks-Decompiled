# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBoardsVehiclesOverlayMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent # Importing BaseDAAPIComponent to inherit its properties and methods

class EventBoardsVehiclesOverlayMeta(BaseDAAPIComponent):

    # Defining a method to change the filter based on the given id
    def changeFilter(self, id):
        self._printOverrideError('changeFilter') # Printing an error message if this method is overridden

    # Defining a method to apply filters based on nation, vehicleType, level, isMain, and hangarOnly
    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._printOverrideError('applyFilters') # Printing an error message if this method is overridden

    # Defining an actionscript method to set the header data
    def as_setHeaderS(self, data):
        return self.flashObject.as_setHeader(data) if self._isDAAPIInited() else None # Returning None if DAAPI is not initialized, otherwise calling the corresponding actionscript method

    # Defining an actionscript method to set the filter data
    def as_setFiltersS(self, data):
        return self.flashObject.as_setFilters(data) if self._isDAAPIInited() else None # Returning None if DAAPI is not initialized, otherwise calling the corresponding actionscript method

    # Defining an actionscript method to set the vehicle data
    def as_setVehiclesS(self, data):
        return self.flashObject.as_setVehicles(data) if self._isDAAPIInited() else None # Returning None if DAAPI is not initialized, otherwise calling the corresponding actionscript method
