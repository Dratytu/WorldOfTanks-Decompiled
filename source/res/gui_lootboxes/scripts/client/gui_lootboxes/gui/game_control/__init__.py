# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/game_control/__init__.py

# Import necessary modules and functions
from gui.shared.system_factory import registerGameControllers  # Function to register game controllers
from gui_lootboxes.gui.game_control.gui_lootboxes_controller import GuiLootBoxesController  # The game controller for gui_lootboxes
from skeletons.gui.game_control import IGuiLootBoxesController  # Interface for the gui_lootboxes game controller

# Function to register gui_lootboxes game controllers
def registerGuiLootBoxesGameControllers():
    # Register the game controller with the system factory using the IGuiLootBoxesController interface,
    # GuiLootBoxesController implementation, and set to auto-create the controller
    registerGameControllers([(IGuiLootBoxesController, GuiLootBoxesController, True)])

