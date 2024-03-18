# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_trade_in.py

# Import necessary modules and classes.
from CurrentVehicle import g_currentPreviewVehicle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelTradeInMeta import VehiclePreviewBottomPanelTradeInMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import event_dispatcher, events
from gui.shared.formatters import getItemPricesVO, text_styles
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from skeletons.gui.game_control import ITradeInController
from skeletons.gui.shared import IItemsCache

# Define the VehiclePreviewBottomPanelTradeIn class.
class VehiclePreviewBottomPanelTradeIn(VehiclePreviewBottomPanelTradeInMeta):
    # Inject dependencies using dependency.descriptor.
    __tradeIn = dependency.descriptor(ITradeInController)
    __itemsCache = dependency.descriptor(IItemsCache)

    # Initialize the class.
    def __init__(self):
        # Call the superclass constructor.
        super(VehiclePreviewBottomPanelTradeIn, self).__init__()
        # Initialize class variables.
        self.__tradeInVehicleToBuy = None
        self.__tradeInVehicleToSell = None
        self.__backAlias = None
        self.__backCallback = None

    # Handle the Buy button click event.
    def onBuyClick(self):
        event_dispatcher.showVehicleBuyDialog(g_currentPreviewVehicle.item, previousAlias=VIEW_ALIAS.TRADE_IN_VEHICLE_PREVIEW, returnCallback=self.__backCallback, returnAlias=self.__backAlias)

    # Set the backAlias for navigating back to the previous screen.
    def setBackAlias(self, backAlias):
        self.__backAlias = backAlias

    # Set the backCallback for handling the back navigation event.
    def setBackCallback(self, backCallback):
        self.__backCallback = backCallback

    # Perform additional actions when the view is populated.
    def _populate(self):
        # Call the superclass _populate() method.
        super(VehiclePreviewBottomPanelTradeIn, self)._populate()
        # Register a callback for the itemsCache.onSyncCompleted event.
        self.__itemsCache.onSyncCompleted += self.__onCacheSyncCompleted
        # Add a listener for the VehicleBuyEvent.VEHICLE_SELECTED event.
        self.addListener(events.VehicleBuyEvent.VEHICLE_SELECTED, self.__updateData)

    # Perform cleanup when the view is disposed.
    def _dispose(self):
        # Remove the listener for the VehicleBuyEvent.VEHICLE_SELECTED event.
        self.removeListener(events.VehicleBuyEvent.VEHICLE_SELECTED, self.__updateData)
        # Unregister the callback for the itemsCache.onSyncCompleted event.
        self.__itemsCache.onSyncCompleted -= self.__onCacheSyncCompleted
        # Call the superclass _dispose() method.
        super(VehiclePreviewBottomPanelTradeIn, self)._dispose()

    # Handle the registration of a flash component.
    def _onRegisterFlashComponent(self, viewPy, alias):
        # Update the data.
        self.__updateData()
        # If the alias matches the expected value, set the tradeInVehicle.
        if alias == VEHPREVIEW_CONSTANTS.TRADE_OFF_WIDGET_ALIAS:
            viewPy.setTradeInVehicle(self.__tradeInVehicleToBuy)

    # Update the data displayed in the view.
    def __updateData(self, _=None):
        # Update the trade vehicles.
        self.__updateTradeVehicles()
        # If the tradeInVehicleToBuy is not None, update the view with the new data.
        if self.__tradeInVehicleToBuy is not None:
            self.as_setDataS(self.__getVO())
        return

    # Get the View Object (VO) for the view.
    def __getVO(self):
        # Calculate the statusText, statusOk, tradeOffAvailable, and isFreeExchange variables.
        statusText, statusOk, tradeOffAvailable, isFreeExchange = self.__getStatus()
        # Return the VO with the calculated values.
        return {'currentPrice': getItemPricesVO(self.__tradeIn.getTradeInPrice(self.__tradeInVehicleToBuy)),
         'selectedPrice': None if isFreeExchange else self.__getSelectedPrice(),
         'statusText': text_styles.greenText(statusText) if isFreeExchange else statusText,
         'statusOk': statusOk,
         'tradeOffAvailable': tradeOffAvailable}

    # Update the trade vehicles.
    def __updateTradeVehicles(self):
        # Set the tradeInVehicleToBuy and tradeInVehicleToSell variables.
        self.__tradeInVehicleToBuy = g_currentPreviewVehicle.item
        self.__tradeInVehicleToSell = self.__tradeIn.getSelectedVehicleToSell()

    # Get the selected price based on the tradeInVehicleToSell.
    def __getSelectedPrice(self):
        # If tradeInVehicleToSell is not None, return the ItemPrice; otherwise, return None.
        return None if self.__tradeInVehicleToSell is None else getItemPricesVO(ItemPrice(self.__tradeInVehicleToSell.tradeOffPrice,
