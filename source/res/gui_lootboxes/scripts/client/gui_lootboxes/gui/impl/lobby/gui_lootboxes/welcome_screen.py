# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/lobby/gui_lootboxes/welcome_screen.py

# Import necessary modules and libraries
from account_helpers.AccountSettings import LOOT_BOXES_INTRO_SHOWN
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.pub.lobby_window import LobbyWindow
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IGuiLootBoxesController
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.welcome_screen_model import WelcomeScreenModel
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.sound import LOOT_BOXES_OVERLAY_SOUND_SPACE

# Define the LootBoxesWelcomeScreen class, which inherits from ViewImpl
class LootBoxesWelcomeScreen(ViewImpl):
    # Inject the IGuiLootBoxesController dependency
    __guiLootBoxes = dependency.descriptor(IGuiLootBoxesController)
    # Define a class variable for the common sound space
    _COMMON_SOUND_SPACE = LOOT_BOXES_OVERLAY_SOUND_SPACE

    def __init__(self):
        # Initialize the ViewImpl class with the given settings
        settings = ViewSettings(R.views.gui_lootboxes.lobby.gui_lootboxes.WelcomeScreen())
        # Set the view model for the class
        settings.model = WelcomeScreenModel()
        super(LootBoxesWelcomeScreen, self).__init__(settings)

    @property
    def viewModel(self):
        # Return the view model of the class
        return super(LootBoxesWelcomeScreen, self).getViewModel()

    def _getEvents(self):
        # Return a tuple of event handlers
        return ((self.viewModel.onClose, self.__onClose),)

    def __onClose(self):
        # Set the LOOT_BOXES_INTRO_SHOWN setting in AccountSettings to True
        self.__guiLootBoxes.setSetting(LOOT_BOXES_INTRO_SHOWN, True)
        # Destroy the window
        self.destroyWindow()


# Define the LootBoxesWelcomeScreenWindow class, which inherits from LobbyWindow
class LootBoxesWelcomeScreenWindow(LobbyWindow):
    # Define the class slots
    __slots__ = ()

    def __init__(self, parent=None):
        # Initialize the L
