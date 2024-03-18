# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/controllers/sound_ctrls/common.py

import typing
import BattleReplay
import BigWorld
import SoundGroups
from Event import EventsSubscriber
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from helpers import dependency, isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider
from shared_utils import nextTick

# Class for managing a set of sound players
class SoundPlayersController(object):

    def __init__(self):
        self._soundPlayers = set()

    def init(self):
        """
        Initialize all sound players.
        """
        for player in self._soundPlayers:
            player.init()

    def destroy(self):
        """
        Destroy all sound players.
        """
        for player in self._soundPlayers:
            player.destroy()

        self._soundPlayers = None
        return


# Abstract class for a battle controller that manages sound players
class SoundPlayersBattleController(IBattleController):

    def __init__(self):
        self.__soundPlayers = self._initializeSoundPlayers()

    def startControl(self, *args):
        """
        Start controlling the sound players.
        """
        self.__startPlayers()

    def stopControl(self):
        """
        Stop controlling the sound players.
        """
        self.__destroyPlayers()

    def getControllerID(self):
        """
        Get the ID of the battle controller.
        """
        return BATTLE_CTRL_ID.SOUND_PLAYERS_CTRL

    def _initializeSoundPlayers(self):
        """
        Implement this method in derived classes to initialize the sound players.
        """
        raise NotImplementedError

    def __startPlayers(self):
        """
        Start all sound players.
        """
        for player in self.__soundPlayers:
            player.init()

    def __destroyPlayers(self):
        """
        Destroy all sound players.
        """
        for player in self.__soundPlayers:
            player.destroy()

        self.__soundPlayers = None
        return


# Abstract class for a sound player
class SoundPlayer(object):

    def init(self):
        """
        Initialize the sound player.
        """
        nextTick(self._subscribe)()

    def destroy(self):
        """
        Destroy the sound player.
        """
        self._stop()
        self._unsubscribe()

    def _subscribe(self):
        """
        Subscribe to necessary events.
        """
        raise NotImplementedError

    def _unsubscribe(self):
        """
        Unsubscribe from events.
        """
        raise NotImplementedError

    @staticmethod
    def _playSound2D(event, checkAlive=False):
        """
        Play a 2D sound.
        """
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        else:
            if checkAlive:
                vehicle = BigWorld.player().getVehicleAttached()
                if vehicle is not None and not vehicle.isAlive():
                    return
            SoundGroups.g_instance.playSound2D(event)
            return


# Sound player for vehicle state events
class VehicleStateSoundPlayer(SoundPlayer):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _subscribe(self):
        """
        Subscribe to vehicle state updates and viewpoint switching events.
        """
        ctrl = self._sessionProvider.shared.vehicleState
        ctrl.onVehicleStateUpdated += self._onVehicleStateUpdated
        BigWorld.player().onSwitchingViewPoint += self._onSwitchViewPoint

    def _unsubscribe(self):
        """
        Unsubscribe from vehicle state updates and viewpoint switching events.
        """
        ctrl = self._sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated -= self._onVehicleStateUpdated
        if isPlayerAvatar():
            BigWorld.player().onSwitchingViewPoint -= self._onSwitchViewPoint
        return

    def _onVehicleStateUpdated(self, state, value):
        """
        Handle vehicle state updates.
        """
        pass

    def _onSwitchViewPoint(self):
        """
        Handle viewpoint switching events.
        """
        pass


# Base class for sound players that play sounds based on efficiency
class BaseEfficiencySoundPlayer(SoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _subscribe(self):
        """
        Subscribe to efficiency updates.
        """
        ctrl = self.__sessionProvider.shared.personalEfficiencyCtrl
        ctrl.onPersonalEfficiencyReceived += self
