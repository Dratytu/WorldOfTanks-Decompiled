# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/hangar/carousel/tank_carousel.py

# Import necessary modules and constants
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import ARENA_BONUS_TYPE
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.Scaleform.daapi.view.common.filter_popover import fillFunRandomFilterVO
from fun_random.gui.Scaleform.daapi.view.lobby.hangar.carousel.carousel_data_provider import FunRandomCarouselDataProvider
from fun_random.gui.Scaleform.daapi.view.lobby.hangar.carousel.carousel_filter import FunRandomCarouselFilter
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel

# Define a function to remove a filter by name
def _removeFilterByName(filters, filterName):
    return tuple((f for f in filters if f != filterName))

# Define the FunRandomTankCarousel class, which inherits from BattlePassTankCarousel and FunSubModesWatcher
class FunRandomTankCarousel(BattlePassTankCarousel, FunSubModesWatcher):

    # Initialize the class
    def __init__(self):
        super(FunRandomTankCarousel, self).__init__()
        self._carouselDPCls = FunRandomCarouselDataProvider
        self._carouselFilterCls = FunRandomCarouselFilter

    # Define a method to get custom parameters
    def getCustomParams(self):
        return {'isBattlePass': self._battlePassController.isGameModeEnabled(ARENA_BONUS_TYPE.FUN_RANDOM)}

    # Define a class method to create a filter VO for the 'funRandom' filter
    @classmethod
    def _makeFilterVO(cls, filterID, contexts, filters):
        return super(FunRandomTankCarousel, cls)._makeFilterVO(filterID, contexts, filters) if filterID != 'funRandom' else fillFunRandomFilterVO({'id': filterID}, filters[filterID], True)

    # Override the _populate method
    def _populate(self):
        super(FunRandomTankCarousel, self)._populate()
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self.startSubSettingsListening(self.__updateVehicles, desiredOnly=True)
        self.startSubSelectionListening(self.__onSubModeSelected)

    # Override the _dispose method
    def _dispose(self):
        self.stopSubSelectionListening(self.__onSubModeSelected)
        self.stopSubSettingsListening(self.__updateVehicles, desiredOnly=True)
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        super(FunRandomTankCarousel, self)._dispose()

    # Override the _getInitialFilterVO method
    def _getInitialFilterVO(self, contexts):
        filtersVO = super(FunRandomTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['popoverAlias'] = FUNRANDOM_ALIASES.FUN_RANDOM_CAROUSEL_FILTER_POPOVER
        return filtersVO

    # Override the _getFilters method
    def _getFilters(self):
        filters = super(FunRandomTankCarousel, self)._getFilters()
        if not BONUS_CAPS.checkAny(ARENA_BONUS_TYPE.FUN_RANDOM, BONUS_CAPS.DAILY_MULTIPLIED_XP):
            filters = _removeFilterByName(filters, 'bonus')
        return filters + ('funRandom',)

    # Define the __onViewLoaded method
    def __onViewLoaded(self, view, *args, **kwargs):
        if view.alias == FUNRANDOM_ALIASES.FUN_RANDOM_CAROUSEL_FILTER_POPOVER:
            view.setTankCarousel(self)

    # Define the __onSubModeSelected method
    def __onSubModeSelected(self, *_):
        if self._carouselDP is not None:
            self._carouselDP.onSubModeSelected()
        self.__updateVehicles()
        return

    # Define the __updateVehicles method
    def __updateVehicles(self, *_):
        self.updateVehicles()
