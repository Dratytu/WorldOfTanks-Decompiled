# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_battle_overlay.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.meta.EventBoardsBattleOverlayMeta import EventBoardsBattleOverlayMeta
from gui.Scaleform.daapi.view.lobby.event_boards.event_summary import getSummaryInfoData

# Define the EventBoardsBattleOverlay class that inherits from EventBoardsBattleOverlayMeta
class EventBoardsBattleOverlay(EventBoardsBattleOverlayMeta):
    # Declare a class variable __opener and initialize it to None
    __opener = None

    # Define a method setOpener to set the opener view and process event data
    def setOpener(self, view):
        # Set the __opener class variable to the provided view
        self.__opener = view
        # Get the context and event data from the opener view
        ctx = self.__opener.ctx
        eventData = self.__opener.eventData
        # Get summary info data by calling the getSummaryInfoData function
        data = getSummaryInfoData(eventData, ctx.get('leaderboard'), ctx.get('excelItem'))
        # Call the as_setDataS method with the header data
        self.as_setDataS(data.getHeader())
        # Call the as_setExperienceDataS method with the experience block data
        self.as_setExperienceDataS(data.getExperienceBlock())
        # Call the as_setStatisticsDataS method with the statistics block data
        self.as_setStatisticsDataS(data.getStatisticsBlock())
        # Check if table data is available and call the corresponding methods
        if data.isTable():
            self.as_setTableHeaderDataS(data.getTableHeaderData())
            self.as_setTableDataS(data.getTableData())
