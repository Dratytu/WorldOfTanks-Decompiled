# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/game_control/__init__.py
from armory_yard.gui.game_control.armory_yard_controller import ArmoryYardController
from armory_yard.gui.game_control.awards_controller import ArmoryYardStyleQuestsHandler
from skeletons.gui.game_control import IArmoryYardController
from gui.shared.system_factory import registerGameControllers, registerAwardControllerHandler

def register_ay_game_controllers():
    register_game_controllers([(IArmoryYardController, ArmoryYardController, False)])


def register_ay_award_controllers():
    register_award_controller_handler(ArmoryYardStyleQuestsHandler)


# Register game and award controllers during the module initialization
register_ay_game_controllers()
register_ay_award_controllers()
