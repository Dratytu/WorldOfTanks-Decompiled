# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_browser_view.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView  # Base class for web-based views
from helpers import dependency  # Helper module for dependency injection
from skeletons.gui.game_control import IBattleRoyaleController  # Interface for the Battle Royale controller
from web.web_client_api.battle_royale import createBattleRoyaleWebHanlders  # Module for creating web handlers for Battle Royale

# Define the BattleRoyaleBrowserView class
class BattleRoyaleBrowserView(WebView):

    # Inject the IBattleRoyaleController dependency
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    # Define the webHandlers method
    def webHandlers(self):
        # Create and return the Battle Royale web handlers
        return createBattleRoyaleWebHanlders()

    # Override the _populate method
    def _populate(self):
        # Call the superclass's _populate method
        super(BattleRoyaleBrowserView, self)._populate()

        # Register the onUpdated callback for the IBattleRoyaleController
        self.__battleRoyaleController.onUpdated += self.__onSettingsChange

    # Override the _dispose method
    def _dispose(self):
        # Call the superclass's _dispose method
        super(BattleRoyaleBrowserView, self)._dispose()

