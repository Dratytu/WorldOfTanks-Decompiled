# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/configurable_vehicle_preview.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from shared_utils import CONST_CONTAINER

# Define a class for storing optional blocks in the vehicle preview
class OptionalBlocks(CONST_CONTAINER):
    # Define the optional blocks
    BUYING_PANEL = 'buyingPanel'
    CLOSE_BUTTON = 'closeBtn'
    # Set all the optional blocks
    ALL = (BUYING_PANEL, CLOSE_BUTTON)


# Inherit from the base VehiclePreview class
class ConfigurableVehiclePreview(VehiclePreview):

    def __init__(self, ctx):
        # Call the constructor of the parent class
        super(ConfigurableVehiclePreview, self).__init__(ctx)
        # Extract hidden blocks from the context
        self.__hiddenBlocks = ctx.get('hiddenBlocks')
        # Determine whether to show the close button
        self.__showCloseBtn = OptionalBlocks.CLOSE_BUTTON not in self.__hiddenBlocks

    # Override the setBottomPanel method
    def setBottomPanel(self):
        # If the buying panel is among the hidden blocks, set an empty bottom panel
        if OptionalBlocks.BUYING_PANEL in self.__hiddenBlocks:
            self.as_setBottomPanelS('')
        # Otherwise, call the parent class's setBottomPanel method
        else:
            super(ConfigurableVehiclePreview, self).setBottomPanel()

    # Override the _getData method
    def _getData(self):
        # Get data from the parent class and add the showCloseBtn attribute
        result = super(ConfigurableVehiclePreview, self)._getData()
        result.update({'showCloseBtn': self.__showCloseBtn})
        # Return the result
        return result

    # Override the _getExitEvent method
   
