# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ItemsWithVehicleFilterTabViewMeta.py

# This is the meta class for the 'ItemsWithVehicleFilterTabView' view, which is a subclass of 'FiltrableInventoryCategoryByTypeTabView'.
# The meta class is used to define the view's interface, which is a contract between the view and the server.
# The interface is defined using action scripts (as\_*), which are methods that start with 'as\_'.

from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_type import FiltrableInventoryCategoryByTypeTabView

class ItemsWithVehicleFilterTabViewMeta(FiltrableInventoryCategoryByTypeTabView):

    # This method resets the vehicle filter for the current tab.
    def resetVehicleFilter(self):
        # The '_printOverrideError' method is called to print an error message if this method is overridden.
        self._printOverrideError('resetVehicleFilter')

    # This action script initializes the vehicle filter for the current tab.
    # 'vehicleFilterVO' is a data object that contains the initial state of the vehicle filter.
    def as_initVehicleFilterS(self, vehicleFilterVO):
        # The 'flashObject' is used to call the 'as\_initVehicleFilter' method on the client-side view.
        # The 'if' statement checks if the DAAPI has been initialized before making the call.
        return self.flashObject.as_initVehicleFilter(vehicleFilterVO) if self._isDAAPIInited() else None

    # This action script updates the state of the vehicle filter button for the current tab.
    # 'vehicleFilterVO' is a data object that contains the updated state of the vehicle filter.
    def as_updateVehicleFilterButtonS(self, vehicleFilterVO):
        # The 'flashObject' is used to call the 'as\_updateVehicleFilterButton' method on the client
