# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/entity.py

import logging # Importing the logging module for logging purposes
from constants import PREBATTLE_TYPE, QUEUE_TYPE # Importing constants for prebattle types and queue types
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle # Importing current vehicle and preview vehicle from the CurrentVehicle module
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events # Importing event bus, event scope, and event classes from the gui.shared module
from gui.impl.gen import R # Importing R for accessing resource files
from helpers import dependency # Importing dependency for dependency injection
from gui.periodic_battles.models import PrimeTimeStatus # Importing PrimeTimeStatus from the periodic battles module
from skeletons.gui.game_control import IBattleRoyaleTournamentController # Importing the IBattleRoyaleTournamentController interface
from skeletons.gui.impl import IGuiLoader # Importing the IGuiLoader interface
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams # Importing GuiImplViewLoadParams for loading scaleform views
from gui.Scaleform.framework import ScopeTemplates # Importing ScopeTemplates for managing scopes
from gui.prb_control.ctrl_events import g_prbCtrlEvents # Importing prb control events
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity, PreQueueEntryPoint, PreQueueSubscriber # Importing base classes for pre-queue entities, entry points, and subscribers
from battle_royale.gui.prb_control.entities.tournament.pre_queue.action_validator import BattleRoyaleTournamentActionsValidator # Importing the action validator for tournament pre-queue
from battle_royale.gui.prb_control.entities.regular.pre_queue.vehicles_watcher import BattleRoyaleVehiclesWatcher # Importing the vehicle watcher for tournament pre-queue
from battle_royale.gui.prb_control.entities.tournament.pre_queue.permissions import BattleRoyaleTournamentPermissions # Importing the permissions for tournament pre-queue
from gui.prb_control.entities.special_mode.pre_queue.ctx import SpecialModeQueueCtx # Importing the special mode queue context
from gui.prb_control.events_dispatcher import g_eventDispatcher # Importing the prb control events dispatcher
from gui.prb_control.settings import FUNCTIONAL_FLAG, PRE_QUEUE_JOIN_ERRORS # Importing functional flags and pre-queue join errors
from gui.prb_control.storages import prequeue_storage_getter # Importing the pre-queue storage getter

_logger = logging.getLogger(__name__) # Creating a logger instance with the current module name

class BattleRoyaleTournamentEntryPoint(PreQueueEntryPoint): # Defining the BattleRoyaleTournamentEntryPoint class that inherits from PreQueueEntryPoint
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController) # Declaring a dependency on IBattleRoyaleTournamentController

    def __init__(self): # Constructor
        super(BattleRoyaleTournamentEntryPoint, self).__init__(FUNCTIONAL_FLAG.BATTLE_ROYALE, QUEUE_TYPE.BATTLE_ROYALE_TOURNAMENT) # Initializing the parent class with functional flag and queue type

    def select(self, ctx, callback=None): # Method for selecting the entry point
        if not self.__battleRoyaleTournamentController.isAvailable(): # Checking if the tournament controller is available
            if callback is not None:
                callback(False)
            g_prbCtrlEvents.onPreQueueJoinFailure(PRE_QUEUE_JOIN_ERRORS.DISABLED) # Failing the join process with the disabled error
            return
        else:
            super(BattleRoyaleTournamentEntryPoint, self).select(ctx, callback) # Proceeding with the selection process
            return

    def _getFilterStates(self): # Method for getting filter states
        return (PrimeTimeStatus.NOT_SET,) # Returning the filter states


class BattleRoyaleTournamentEntity(PreQueueEntity): # Defining the BattleRoyaleTournamentEntity class that inherits from PreQueueEntity
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController) # Declaring a dependency on IBattleRoyaleTournamentController
    __gui = dependency.descriptor(IGuiLoader) # Declaring a dependency on IGuiLoader

    def __init__(self): # Constructor
        super(BattleRoyaleTournamentEntity, self).__init__(FUNCTIONAL_FLAG.BATTLE_ROYALE, QUEUE_TYPE.BATTLE_ROYALE_TOURNAMENT, PreQueueSubscriber()) # Initializing the parent class with functional flag, queue type, and subscriber
