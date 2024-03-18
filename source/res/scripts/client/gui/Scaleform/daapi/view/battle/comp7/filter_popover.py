# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/filter_popover.py

# Import necessary modules
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE
from gui.Scaleform.daapi.view.battle.comp7.common import getSavedRowCountValue, rowValueToRowCount, rowCountToRowValue
from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover, FILTER_SECTION
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles

# Define the Comp7TankCarouselFilterPopover class, which inherits from TankCarouselFilterPopover
class Comp7TankCarouselFilterPopover(TankCarouselFilterPopover):

    # Override the switchCarouselType method
    def switchCarouselType(self, selected):
        # Set the carouselRowCount attribute based on the selected value
        self._carouselRowCount = 1 if selected else 0
        # Save the carouselRowCount value
        self.__saveRowCountValue()
        # Set the row count of the carousel to the corresponding value
        self._carousel.setRowCount(rowValueToRowCount(self._carouselRowCount))

    # Override the _populate method
    def _populate(self):
        # Call the superclass's implementation of the _populate method
        super(Comp7TankCarouselFilterPopover, self)._populate()
        # Enter gui control mode for the Comp7 Tank Carousel Filter Popover
        self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER, enableAiming=False)

    # Override the _dispose method
    def _dispose(self):
        # Leave gui control mode for the Comp7 Tank Carousel Filter Popover
        self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER)
        # Call the superclass's implementation of the _dispose method
        super(Comp7TankCarouselFilterPopover, self)._dispose()

    # Override the _readRowCount method
    def _readRowCount(self, ctx):
        # Get the saved row value and whether it was saved by the player
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        # If the row value was saved by the player, set the carouselRowCount attribute to the saved value
        if isSavedByPlayer:
            self._carouselRowCount = savedRowValue
        # If the context has a data attribute, set the carouselRowCount attribute based on the row count in the context
        elif ctx and 'data' in ctx:
            data = ctx['data']
            self._carouselRowCount = rowCountToRowValue(getattr(data, 'rowCount', 1))

    # Override the _saveRowCount method
    def _saveRowCount(self):
        # Get the saved row value and whether it was saved by the player
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        # If the saved row value was not set by the player and the current carouselRowCount value is different, save the current value
        if isSavedByPlayer and savedRowValue != self._carouselRowCount:
            self.__saveRowCountValue()

    # Override the _getInitialVO method
    def _getInitialVO(self, filters, xpRateMultiplier):
        # Call the superclass's implementation of the _getInitialVO method
        dataVO = super(Comp7TankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        # Set the specialSectionVisible attribute of the dataVO to True
        dataVO['specialSectionVisible'] = True
        # Set the searchSectionVisible attribute of the dataVO to True
        dataVO['searchSectionVisible'] = True
        # Set the progressionsSectionVisible attribute of the dataVO to False
        dataVO['progressionsSectionVisible'] = False
        # Set the additionalInfo attribute of the dataVO to a text style containing a description of the battle carousel filter popover
        dataVO['additionalInfo'] = text_styles.stats(backport.text(R.strings.comp7.battleCarousel.filterPopover.desc()))
        # Get the vehicle levels filter from the carousel
        vehicleLevels = self._carousel.getCustomParams().get('vehicleLevelsFilter', list())
        # If the carousel is not None and there is only one vehicle level in the filter, set the tankTierSectionVisible attribute of the dataVO to False
        if self._carousel is not None and not len(vehicleLevels) > 1:
            dataVO['tankTierSectionVisible'] = False
        # Return the modified dataVO
        return
