# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/repository.py

# Import necessary modules and classes
from gui.battle_control.controllers import battle_field_ctrl, debug_ctrl, default_maps_ctrl, perk_ctrl
from gui.battle_control.controllers.repositories import _ControllersRepository, registerBattleControllerRepo
from battle_royale.gui.battle_control.controllers import spawn_ctrl, vehicles_count_ctrl, radar_ctrl, progression_ctrl, death_ctrl
from battle_royale.gui.battle_control.controllers.battle_royale_appearance_cache_ctrl import BattleRoyaleAppearanceCacheController
from constants import ARENA_GUI_TYPE

class BattleRoyaleControllersRepository(_ControllersRepository):
    """
    A class that inherits from _ControllersRepository and is used to manage battle controllers for the Battle Royale game mode.
    """
    __slots__ = ()  # No additional instance variables

    @classmethod
    def create(cls, setup):
        """
        Creates an instance of BattleRoyaleControllersRepository and adds various view controllers and arena view controllers to it.
        :param setup: A setup object containing necessary information for creating the repository
        :return: An instance of BattleRoyaleControllersRepository
        """
        repository = super(BattleRoyaleControllersRepository, cls).create(setup)
        repository.addArenaViewController(progression_ctrl.ProgressionController(), setup)
        repository.addArenaViewController(battle_field_ctrl.BattleFieldCtrl(), setup)
        repository.addViewController(perk_ctrl.PerksController(), setup)
        repository.addViewController(spawn_ctrl.SpawnController(), setup)
        repository.addViewController(debug_ctrl.DebugController(), setup)
        repository.addArenaViewController(vehicles_count_ctrl.VehicleCountController(), setup)
        repository.addViewController(default_maps_ctrl.DefaultMapsController(setup), setup)
        repository.addArenaController(BattleRoyaleAppearanceCacheController(setup), setup)
        repository.addArenaController(death_ctrl.DeathScreenController(), setup)
