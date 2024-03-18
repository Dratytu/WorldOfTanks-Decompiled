# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/__init__.py

# Import necessary modules and classes
from battle_royale.gui.game_control.battle_royale_controller import BattleRoyaleController as _BattleRoyale
from battle_royale.gui.game_control.battle_royale_tournament_controller import BattleRoyaleTournamentController as _BRTournament
from battle_royale.gui.game_control.battle_royale_rent_vehicles_controller import BattleRoyaleRentVehiclesController as _BRRentController
import skeletons.gui.game_control as _interface  # Skeleton interface for game control
from gui.shared.system_factory import registerGameControllers  # Function to register game controllers

# Function to register Battle Royale game controllers
def registerBRGameControllers():
    # Register the following game controllers using the 'registerGameControllers' function:
    # 1. IBattleRoyaleController: BattleRoyaleController
    # 
