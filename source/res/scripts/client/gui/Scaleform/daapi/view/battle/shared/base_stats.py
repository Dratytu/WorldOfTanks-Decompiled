# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.py

# Import necessary modules and classes.
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.shared import events  # Events module for handling game events
from helpers import dependency  # For dependency injection
from skeletons.gui.battle_session import IBattleSessionProvider  # Session provider interface

# Define the StatsBase class, inheriting from StatsBaseMeta.
class StatsBase(StatsBaseMeta):
    # Inject the IBattleSessionProvider dependency.
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Property to check if the stats have tabs.
    @property
    def hasTabs(self):
        return False

    # Method to accept a squad session invitation.
    def acceptSquad(self, sessionID):
        self.sessionProvider.invitations.accept(sessionID)

    # Method to send a request to join a squad session.
    def addToSquad(self, sessionID):
        self.sessionProvider.invitations.send(sessionID)

    # Method called when visibility is toggled.
    def onToggleVisibility(self, isVisible):
        self._onToggleVisibility(isVisible)

    # Overridden method for populating the stats.
    def _populate(self):
        # Add event listeners for showing and hiding the cursor.
        self.addListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        # Call the superclass method for further populating.
        super(StatsBase, self)._populate()

    # Overridden method for disposing the stats.
    def _dispose(self):
        # Clean up event listeners and other resources.
        self.__invitations = None
        self.removeListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._dispose()
        return

    # Method called when visibility is toggled.
    def _onToggleVisibility(self, isVisible):
        pass

    # Method called when the cursor is shown.
