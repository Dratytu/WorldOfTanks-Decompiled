# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/hangar/carousel/carousel_filter.py

# Import necessary modules and constants
from account_helpers.AccountSettings import BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2, FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import EventCriteriesGroup
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_filter import BattlePassCarouselFilter, BattlePassCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA

# Define the FunRandomCarouselFilter class, which inherits from BattlePassCarouselFilter
class FunRandomCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        # Call the constructor of the parent class
        super(FunRandomCarouselFilter, self).__init__()

        # Initialize the serverSections attribute with a tuple of filter constants
        self._serverSections = (FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1)

        # Initialize the clientSections attribute with a tuple of filter constants
        self._clientSections = (FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)

        # Initialize the criteriasGroups attribute with a tuple of EventCriteriesGroup and FunRandomCriteriesGroup instances
        self._criteriesGroups = (EventCriteriesGroup(), FunRandomCriteriesGroup())

# Define the FunRandomCriteriesGroup class, which inherits from BattlePassCriteriesGroup and FunSubModesWatcher
class FunRandomCriteriesGroup(BattlePassCriteriesGroup, FunSubModesWatcher):

    def update(self, filters):
        # Call the update method of the parent class
        super(FunRandomCriteriesGroup, self).update(filters)

        # Call the private method __addFunRandomCriteria with the filters argument
       
