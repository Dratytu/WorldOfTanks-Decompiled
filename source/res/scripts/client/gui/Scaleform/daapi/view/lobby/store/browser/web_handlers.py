# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/web_handlers.py

# Import necessary modules and classes
from gui.shared.event_dispatcher import showShop  # A function to open the in-game shop
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS  # A module containing constants for view aliases

# Import web client API modules
from web.web_client_api import webApiCollection  # A class for creating a collection of web API classes
from web.web_client_api.clans import ClansWebApi  # A module for managing clans
from web.web_client_api.platform import PlatformWebApi  # A module for managing platform-specific features
from web.web_client_api.quests import QuestsWebApi  # A module for managing quests
from web.web_client_api.loot_boxes import LootBoxWebApi  # A module for managing loot boxes
from web.web_client_api.ranked_battles import RankedBattlesWebApi  # A module for managing ranked battles
from web.web_client_api.request import RequestWebApi  # A module for making web requests
from web.web_client_api.sound import SoundWebApi, SoundStateWebApi, HangarSoundWebApi  # Modules for managing sounds
from web.web_client_api.shop import ShopWebApi  # A module for managing the in-game shop
from web.web_client_api.hero_tank import HeroTankWebApi  # A module for managing hero tanks
from web.web_client_api.battle_pass import BattlePassWebApi  # A module for managing battle passes
from web.web_client_api.ui import NotificationWebApi, OpenWindowWebApi, OpenTabWebApi, CloseWindowWebApi, UtilWebApi  # Modules for managing UI elements
from web.web_client_api.frontline import FrontLineWebApi  # A module for managing frontline features
from web.web_client_api.blueprints_convert_sale import BlueprintsConvertSaleWebApi  # A module for managing blueprint conversions and sales
from web.web_client_api.uilogging import UILoggingWebApi  # A module for managing UI logging

class _OpenTabWebApi(OpenTabWebApi):
    # Override the _getVehiclePreviewReturnAlias method to return the VIEW_ALIAS.LOBBY_STORE constant
    def _getVehiclePreviewReturnAlias(self, cmd):
        return VIEW_ALIAS.LOBBY_STORE

    # Override the _getVehiclePreviewReturnCallback method to return a callback function that opens the shop
    def _getVehiclePreviewReturnCallback(self, cmd):
        return self.__getReturnCallback(cmd.back_url)

    # Override the _getVehicleStylePreviewCallback method to return a callback function that opens the shop
    def _getVehicleStylePreviewCallback(self, cmd):
        return self.__getReturnCallback(cmd.back_url)

    # Define a helper method to create a callback function that opens the shop
    def __getReturnCallback(self, backUrl):
        return (lambda : showShop(backUrl)) if backUrl is not None else None

# Define a function to create a collection of web API classes

