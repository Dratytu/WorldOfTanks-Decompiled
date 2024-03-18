# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/GUILootboxesPersonality.py

# Import necessary modules and classes
from gui_lootboxes.gui.Scaleform import registerLootboxesTooltipsBuilders
from gui_lootboxes.gui.game_control import registerGuiLootBoxesGameControllers
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.entry_point_view import LootBoxesEntryPointWidget
from gui_lootboxes.messenger.formatters.collections_by_type import registerLootBoxClientFormatters, registerLootBoxServerFormatters
from gui_lootboxes.notification import registerClientNotificationListener, registerClientNotificationHandler
from gui.impl.gen import R
from gui.shared.system_factory import registerCarouselEventEntryPoint

# The preInit function initializes various components and subsystems related to GUILootboxes
def preInit():
    # Register the carousel event entry point for the GUILootboxes lobby
    registerCarouselEventEntryPoint(R.views.gui_lootboxes.lobby.gui_lootboxes.EntryPointView(), LootBoxesEntryPointWidget)
    
    # Register tooltips builders for GUILootboxes
    registerLootboxesTooltipsBuilders()
    
    # Register game controllers for GUILootboxes
    registerGuiLootBoxesGameControllers()
    
    # Register client notification listener for GUILootboxes
    registerClientNotificationListener()
    
    # Register client notification handler for GUILootboxes
    registerClientNotificationHandler()
    
    # Register client formatters for GUILootboxes
    registerLootBoxClientFormatters()
    
    # Register server formatters for GUILootboxes
    registerLootBoxServerFormatters()

# The init function initializes the GUILootboxes system
def init():
    pass

# The start function starts the GUILootboxes system
def start():
