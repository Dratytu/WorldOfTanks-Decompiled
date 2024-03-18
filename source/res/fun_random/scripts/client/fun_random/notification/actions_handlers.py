# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/notification/actions_handlers.py

# Import necessary modules and classes
from adisp import adisp_process
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher, FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasMultipleSubModes
from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from skeletons.gui.lobby_context import ILobbyContext

# Define the SelectFunRandomMode class, which inherits from NavigationDisabledActionHandler and FunSubModesWatcher
class SelectFunRandomMode(NavigationDisabledActionHandler, FunSubModesWatcher):
    # Declare dependency on ILobbyContext
    __lobbyContext = dependency.descriptor(ILobbyContext)

    # Class method to get the notification type
    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    # Class method to define the actions
    @classmethod
    def getActions(cls):
        pass

    # Method to check if header navigation is possible
    @hasMultipleSubModes(defReturn=True)
    def checkHeaderNavigation(self):
        return False

    # Method to handle the action, which navigates to the fun random battle
    @adisp_process
    def doAction(self, model, entityID, action):
        navigationPossible = True
        # Check if header navigation is possible
        if self.checkHeaderNavigation():
            navigationPossible = yield self.__lobbyContext.isHeaderNavigationPossible()
        # If navigation is possible, navigate to the fun random battle
        if navigationPossible:
            yield self.selectFunRandomBattle()


# Define the ShowFunRandomProgression class, which inherits from NavigationDisabledActionHandler and FunProgressionWatcher
class ShowFunRandomProgression(NavigationDisabledActionHandler, FunProgressionWatcher):

    # Class method to get the notification type
    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    # Class method to define the actions
    @classmethod
    def getActions(cls):
        pass

    # Method to handle the action, which shows the active progression page
    def doAction(self, model, entityID, action):
        self.showActiveProgressionPage()
