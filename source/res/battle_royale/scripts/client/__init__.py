# This is the entry point for the battle_royale application.
# The script imports all necessary modules and sets up the application.

# Import required modules
import logging
import sys
from importlib import import_module

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Import game modules
game_modules = ['game.settings', 'game.player', 'game.arena', 'game.gameplay']
for module_name in game_modules:
    try:
        import_module(module_name)
        logger.info(f'Successfully imported {module_name}')
    except Exception as e:
        logger.error(f'Failed to import {module_name}: {e}')
        sys.exit(1)

# Initialize game
game = import_module('game.game').Game()
game.start()
