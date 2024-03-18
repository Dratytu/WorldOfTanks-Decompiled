# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/vehicle_selector.py

# Import necessary modules and classes
from account_helpers.AccountSettings import MISSION_SELECTOR_FILTER, AccountSettings
from gui.Scaleform import getButtonsAssetPath
from gui.Scaleform.daapi.view.lobby.missions.vehicle_selector import MissionVehicleSelector, MissionVehicleSelectorCarousel, SelectorCriteriesGroup
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import CarouselFilter, EventCriteriesGroup
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER
from gui.server_events import caches
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as ms

# Define RegularMissionVehicleSelector class, which inherits from MissionVehicleSelector
class RegularMissionVehicleSelector(MissionVehicleSelector):

    # Override _getTitle method to provide a custom title for the vehicle selector
    def _getTitle(self):
        suitableVehiclesCount = self._carousel.getSuitableVehiclesCount()
        totalVehiclesCount = self._carousel.getTotalVehiclesCount()
        if suitableVehiclesCount == 0:
            suitableStyle = text_styles.unavailable
        else:
            suitableStyle = text_styles.highTitle
        count = '{} / {}'.format(suitableStyle(suitableVehiclesCount), text_styles.main(totalVehiclesCount))
        return text_styles.highTitle(ms(QUESTS.MISSIONS_VEHICLESELECTOR_TITLE, count=count))

    # Static class method _getCarouselAlias, which returns the alias for the carousel
    @classmethod
    def _getCarouselAlias(cls):
        return QUESTS_ALIASES.VEHICLE_SELECTOR_CAROUSEL_ALIAS

    # Override _getNotAvailableStatusText method to provide a custom message when no vehicles are available
    def _getNotAvailableStatusText(self):
        return text_styles.error(QUESTS.MISSIONS_VEHICLESELECTOR_STATUS_NOTAVAILABLE)

# Define RegularVehicleSelectorCarousel class, which inherits from MissionVehicleSelectorCarousel
class RegularVehicleSelectorCarousel(MissionVehicleSelectorCarousel):

    # Initialize the class with a custom carousel filter class
    def __init__(self):
        super(RegularVehicleSelectorCarousel, self).__init__()
        self._carouselFilterCls = _RegularCarouselFilter

    # Override _setCarouselFilters method to set custom filters for the carousel
    def _setCarouselFilters(self):
        filters = self.filter.getFilters(self._usedFilters)
        self.as_initCarouselFilterS({'isVisible': True,
         'mainBtn': {'value': getButtonsAssetPath('params'),
                     'tooltip': TANK_CAROUSEL_FILTER.TOOLTIP_PARAMS},
         'hotFilters': [{'value': QUESTS.QUESTS_TABLE_INHANGAR,
                         'tooltip': TANK_CAROUSEL_FILTER.TOOLTIP_INVENTORY,
                         'selected': filters['inventory']}]})

# Define a custom carousel filter class, which inherits from CarouselFilter
class _RegularCarouselFilter(CarouselFilter):

    # Initialize the class with custom server sections and criteria groups
    def __init__(self):
        super(_RegularCarouselFilter, self).__init__()
        self._serverSections += (MISSION_SELECTOR_FILTER,)
        self._criteriesGroups = (EventCriteriesGroup(), SelectorCriteriesGroup())

    # Override load method to load custom filters from the user's account settings
    def load(self):
        filters = AccountSettings.getFilterDefaults(self._serverSections)
        for section in self._clientSections:
            filters.update(AccountSettings.getFilterDefault(section))

        filters.update(caches.getNavInfo().getVehicleSelectorFilters())
        self._filters = filters
        self.update(filters, save=False)

    # Override save method to save custom filters to the user's account settings
    def save(self):
        filters = AccountSettings.getFilterDefault(MISSION_SELECTOR_FILTER)
        filters = {key:value for key, value in self._filters.iteritems() if key in filters}
        caches.getNavInfo().setVehicleSelectorFilters(filters)
