# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_filter_popover.py

# Import necessary modules
from gui.Scaleform.daapi.view.meta.EventBoardsResultFilterPopoverViewMeta import EventBoardsResultFilterPopoverViewMeta
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.shared.utils.functions import makeTooltip
from .event_boards_vos import makeFiltersVO

# Define the EventBoardsFilterPopover class, which inherits from EventBoardsResultFilterPopoverViewMeta
class EventBoardsFilterPopover(EventBoardsResultFilterPopoverViewMeta):
    
    def __init__(self, ctx=None):
        # Call the constructor of the superclass
        super(EventBoardsFilterPopover, self).__init__(ctx)
        
        # Extract data from the context, if available
        data = ctx.get('data')
        self.caller = data.caller if data else None
        self.eventID = data.eventID if data else None
        
        # Initialize the onChangeFilter method reference as None
        self.__onChangeFilter = None
        
    def changeFilter(self, lid):
        # Call the onChangeFilter method with the lid as an argument
        self.__onChangeFilter(int(lid))

    def onWindowClose(self):
        # Destroy the popover when the window is closed
        self.destroy()

    def setData(self, eventData, onApply, leaderboardID=None):
        # Set the onChangeFilter method reference to onApply
        self.__onChangeFilter = onApply
        
        # Extract eventType and leaderboards from the eventData
        eventType = eventData.getType()
        leaderboards = eventData.getLeaderboards()
        
        # If leaderboardID is not provided, use the first leaderboard ID
        if leaderboardID is None:
            leaderboardID = leaderboards[0][0]
        
        # Prepare data to be sent to the popover
        data = {
            'filters': makeFiltersVO(eventType, leaderboards, leaderboardID),
            'tooltip': makeTooltip(EVENT_BOARDS.POPOVER_BUTTONS_RATING, '#event
