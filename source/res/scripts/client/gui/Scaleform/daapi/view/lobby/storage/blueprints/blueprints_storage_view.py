# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/blueprints/blueprints_storage_view.py

import nations
from blueprints.BlueprintTypes import BlueprintTypes
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.blueprints import (
    BlueprintsStorageCarouselDataProvider,
    blueprintExitEvent,
    BlueprintsStorageCarouselFilter
)
from gui.Scaleform.daapi.view.lobby.storage.storage_carousel_environment import StorageCarouselEnvironment
from gui.Scaleform.daapi.view.meta.StorageCategoryBlueprintsViewMeta import StorageCategoryBlueprintsViewMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.utils.requesters.blueprints_requester import getNationalFragmentCD
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.STORAGE import STORAGE
from gui import GUI_NATIONS
from WeakMethod import WeakMethodProxy
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class StorageCategoryBlueprintsView(StorageCategoryBlueprintsViewMeta, StorageCarouselEnvironment):
    """
    The view for displaying and managing blueprints in the storage.
    """
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self):
        """
        Initialize the view and set up necessary event listeners.
        """
        super(StorageCategoryBlueprintsView, self).__init__()
        self.__needToResetScrollTo = True

    def navigateToBlueprintScreen(self, itemId):
        """
        Navigate to the blueprint details screen for the given item ID.
        """
        self.filter.update({'scroll_to': itemId})
        self.__needToResetScrollTo = False
        shared_events.showBlueprintView(itemId, blueprintExitEvent())

    def selectConvertible(self, value):
        """
        Update the filter to show only convertible blueprints.
        """
        self.filter.update({'can_convert': value})
        self.applyFilter()

    def _populate(self):
        """
        Set up the data provider, view, and event listeners for the blueprint storage view.
        """
        super(StorageCategoryBlueprintsView, self).setDataProvider(self._dataProvider)
        super(StorageCategoryBlueprintsView, self)._populate()
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self._dataProvider.setEnvironment(self.app)
        g_clientUpdateManager.addCallbacks({'blueprints': self.__onUpdateBlueprints,
         'serverSettings.blueprints_config.levels': self.__onUpdateBlueprints})
        self.__currentFilteredVehicles = self._dataProvider.getCurrentVehiclesCount()
        self.__isFilterCounterShown = False
        self.__updateUniversalFragments()
        self.updateSearchInput(self.filter.get('searchNameVehicle'))
        self.__updateVehicles()
        self.__restoreCarouselState()
        self.updateCounter()

    def _dispose(self):
        """
        Clean up event listeners and other resources when the view is closed.
        """
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        g_clientUpdateManager.removeObjectCallbacks(self)
        if self.__needToResetScrollTo:
            self.filter.update({'can_convert': False})
        super(StorageCategoryBlueprintsView, self)._dispose()
        super(StorageCategoryBlueprintsView, self).clear()

    def _createDataProvider(self):
        """
        Create and return the data provider for the blueprint storage view.
        """
        return BlueprintsStorageCarouselDataProvider(
            BlueprintsStorageCarouselFilter(),
            self._itemsCache,
            WeakMethodProxy(self.__updateFilterWarning)
        )

    def _onCacheResync(self, reason, diff):
        """
        Handle a resync of the game cache.
        """
        if reason == CACHE_SYNC_REASON.CLIENT_UPDATE:
            self._dataProvider.buildList()
            self.updateCounter()
        if GUI_ITEM_TYPE.VEHICLE in diff:
            self.__updateVehicles(diff.get(GUI_ITEM_TYPE.VEHICLE))

    @staticmethod
    def __makeFragmentVO(count, iconName, tooltipData=None):
        """
        Create a view object for displaying fragment information.
        """
        style = text_styles.stats if count > 0 else text_styles.main
        label = style(backport.getIntegralFormat(count))
        return {
            'hasFragments': count > 0,
            'label': label,
            'iconSmall': RES_ICONS.getBlueprintFragment('small', iconName),
            'iconBig': RES_ICONS.getBlueprintFragment('big', iconName),
            'tooltipData': tooltipData
        }

    def __onViewLoaded(self, view, *args, **kwargs):
        """
        Handle the loading of related views.
        """
        if view.settings is not None and view.settings.alias == VIEW_ALIAS.STORAGE_BLUEPRINTS_FILTER_POPOVER:
            view.setTankCarousel(self)
        return

    def __onUpdateBlueprints(self, _):
        """
        Handle updates to the blueprint data.
        """
        self.__updateVehicles()
