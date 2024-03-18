# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/game_control/__init__.py

# Import necessary modules and classes
from armory_yard.gui.game_control.armory_yard_controller import ArmoryYardController  # The main controller for the Armory Yard feature
from armory_yard.gui.game_control.awards_controller import ArmoryYardStyleQuestsHandler  # Handles awards for Armory Yard Style Quests
from skeletons.gui.game_control import IArmoryYardController  # Interface for the Armory Yard controller
from gui.shared.system_factory import registerGameControllers, registerAwardControllerHandler  # Helper functions for registering game and award controllers

# Function to register Armory Yard game controllers
def register_ay_game_controllers():
    # Register the game controllers using the provided interface, controller class, and whether or not the controller is a singleton
    register_game_controllers(
        [(IArmoryYardController, ArmoryYardController, False)]
    )


# Function to register Armory Yard award controllers
def register_ay_award_controllers():
    # Register the award controller handler for Armory Yard Style Quests
    register_award_controller_handler(ArmoryYardStyleQuestsHandler)


# Register game and award controllers during the module initialization
register_ay_game_controllers()
register_ay_award_controllers()

