# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleRoomWindowMeta.py

# Import the RallyMainWindowWithSearch class from the gui.Scaleform.daapi.view.lobby.rally package
from gui.Scaleform.daapi.view.lobby.rally.RallyMainWindowWithSearch import RallyMainWindowWithSearch

# Define the FortBattleRoomWindowMeta class, which inherits from RallyMainWindowWithSearch
class FortBattleRoomWindowMeta(RallyMainWindowWithSearch):

    # Define the onBrowseClanBattles method, which prints an error message indicating that the method is overridden
    def onBrowseClanBattles(self):
        self._printOverrideError('onBrowseClanBattles')

    # Define the onJoinClanBattle method, which prints an error message indicating that the method is overridden
    def onJoinClanBattle(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError('onJoinClanBattle')

    # Define the onCreatedBattleRoom method, which prints an error message indicating that the method is overridden
    def onCreatedBattleRoom(self, battleID, peripheryId):
        self._printOverrideError('onCreatedBattleRoom')

    # Define the refresh method, which prints an error message indicating that the method is overridden
    def refresh(self):
        self._printOverrideError('refresh')

    # Define the as_setWindowTitleS method, which returns the result of calling the as_setWindowTitle method on the flashObject, if the DAAPI is initialized
    def as_setWindowTitleS(self, value):
        return self.flashObject.as_setWindowTitle(value) if self._isDAAPIInited() else None

    # Define the as_setWaitingS method, which returns the result of calling the as_setWaiting method on the flashObject, if the DAAPI is initialized
    def as_setWaitingS(
