# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/managers/GlobalVarsManager.py

# Import necessary modules
import constants
from gui import GUI_SETTINGS
from gui.Scaleform.framework.entities.abstract.GlobalVarsMgrMeta import GlobalVarsMgrMeta
from helpers import getClientOverride
from skeletons.gui.game_control import IWalletController, ITradeInController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.tutorial import ITutorialLoader

# Define the GlobalVarsManager class that inherits from GlobalVarsMgrMeta
class GlobalVarsManager(GlobalVarsMgrMeta):
    # Declare dependency on IItemsCache, IWalletController, ITradeInController, ILobbyContext, and ITutorialLoader
    _isLoginLoadInfoRequested = False
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)
    tradeIn = dependency.descriptor(ITradeInController)
    lobbyContext = dependency.descriptor(ILobbyContext)
    __tutorialLoader = dependency.descriptor(ITutorialLoader)

    # Define a method to check if the game is in development mode
    def isDevelopment(self):
        return constants.IS_DEVELOPMENT

    # Define a method to check if the language bar is visible
    def isShowLangaugeBar(self):
        return GUI_SETTINGS.isShowLanguageBar

    # Define a method to check if server stats are visible
    def isShowServerStats(self):
        return constants.IS_SHOW_SERVER_STATS

    # Define a method to check if the game is running in China
    def isChina(self):
        return constants.IS_CHINA

    # Define a method to check if the game is running in Korea
    def isKorea(self):
        return constants.IS_KOREA

    # Define a method to check if a specific tutorial is running
    def isTutorialRunning(self, tutorialID):
        return self.__tutorialLoader.isRunning and self.__tutorialLoader.tutorialID == tutorialID

    # Define a method to check if free XP to tankman conversion is enabled
    def isFreeXpToTankman(self):
        return self.itemsCache.items.shop.freeXPToTManXPRate > 0

    # Define a method to get the locale override
    def getLocaleOverride(self):
        return getClientOverride()

    # Define a method to check if roaming is enabled
    def isRoamingEnabled(self):
        return self.lobbyContext.getServerSettings().roaming.isEnabled()

    # Define a method to check if the player is currently in roaming
    def isInRoaming(self):
        return self.lobbyContext.getServerSettings().roaming.isInRoaming()

    # Define a method to check if the wallet is available
    def isWalletAvailable(self):
        return self.wallet.isAvailable if self.wallet else False

    # Define a method to check if the login RSS feed is visible
    def isShowLoginRssFeed(self):
        return GUI_SETTINGS.loginRssFeed.show

    # Define a method to check if rentals are enabled
    def isRentalsEnabled(self):
        return constants.IS_RENTALS_ENABLED

    # Define a method to check if personal missions are enabled
    def isPersonalMissionsEnabled(self):
        return self.lobbyContext.getServerSettings().isPersonalMissionsEnabled()

    # Define a method to check if the login info has been loaded at first time
    def isLoginLoadedAtFirstTime(self):
        if GlobalVarsManager._isLoginLoadInfoRequested:
            return False
        GlobalVarsManager._isLoginLoadInfoRequested = True
        return True

    # Define a method to check if vehicle restore is enabled
    def isVehicleRestoreEnabled(self):
        return self.lobbyContext.getServerSettings().isVehicleRestoreEnabled()

    # Define a method to check if
