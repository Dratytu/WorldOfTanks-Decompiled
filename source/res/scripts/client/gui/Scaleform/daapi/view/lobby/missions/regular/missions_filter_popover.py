# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_filter_popover.py

# Import necessary modules
from account_helpers.AccountSettings import AccountSettings, MISSIONS_PAGE
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import HIDE_DONE, HIDE_UNAVAILABLE
from gui.Scaleform.daapi.view.meta.MissionsFilterPopoverViewMeta import MissionsFilterPopoverViewMeta
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import MissionsEvent
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from helpers.i18n import makeString as _ms

# Define the MissionsFilterPopoverView class
class MissionsFilterPopoverView(MissionsFilterPopoverViewMeta):

    # Class constructor
    def __init__(self, ctx=None):
        # Initialize class variables
        self.__filterData = None
        # Call the superclass constructor
        super(MissionsFilterPopoverView, self).__init__()
        return

    # Handle filter change event
    def changeFilter(self, hideUnavailable, hideDone):
        # Create new filter data dictionary
        newData = {HIDE_DONE: hideDone,
                   HIDE_UNAVAILABLE: hideUnavailable}
        # If new data is different from current filter data
        if self.__filterData != newData:
            # Update current filter data
            self.__filterData = newData
            # Save filter data to account settings
            AccountSettings.setFilter(MISSIONS_PAGE, self.__filterData)
            # Fire ON_FILTER_CHANGED event
            self.fireEvent(MissionsEvent(MissionsEvent.ON_FILTER_CHANGED, ctx=self.__filterData), EVENT_BUS_SCOPE.LOBBY)

    # Reset filter to default values
    def setDefaultFilter(self):
        self.changeFilter(False, False)

    # Override _populate method
    def _populate(self):
        # Load filter data from account settings
        self.__filterData = AccountSettings.getFilter(MISSIONS_PAGE)
        # Call superclass _populate method
        super(MissionsFilterPopoverView, self)._populate()
        # Set initial view data
        self.as_setInitDataS(self.__getInitialVO())
        # Set filter data to the view
        self.as_setStateS(self.__filterData)

    # Override _dispose method
    def _dispose(self):
        # Fire ON_FILTER_CLOSED event
        self.fireEvent(MissionsEvent(MissionsEvent.ON_FILTER_CLOSED), EVENT_BUS_SCOPE.LOBBY)
        # Clear filter data
        self.__filterData = None
        # Call superclass _dispose method
        super(MissionsFilterPopoverView, self)._dispose()
        return

    # Prepare initial view data
    def __getInitialVO(self):
        dataVO = {'titleLabel': text_styles.highTitle(QUESTS.MISSIONS_FILTER_POPOVER_TITLE),
                  'hideDoneLabel': _ms(QUESTS.MISSIONS_FILTER_POPOVER_HIDEDONE),
                  'hideUnavailableLabel': _ms(QUESTS.MISSIONS_FILTER_POPOVER_HIDEUNAVAILABLE),
                  'defaultButtonLabel': _ms(QUESTS.MISSIONS_FILTER_POPOVER_DEFAULTBUTTON_LABEL),
                  'defaultButtonTooltip': makeTooltip(QUESTS.MISSIONS_FILTER_POPOVER_DEFAULTBUTTON_HEADER, QUESTS.MISSIONS_FILTER_P
