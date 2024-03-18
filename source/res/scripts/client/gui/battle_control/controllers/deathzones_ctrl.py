# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/controllers/deathzones_ctrl.py

import namedtuple
from collections import defaultdict
import BigWorld
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID

# Define a namedtuple to store timers data for each death zone
_TimersData = namedtuple('_TimersData', 'timeToStrike waveDuration')

class DeathZonesController(IArenaLoadController):
    """
    A controller for managing death zone warnings in the battle.
    """

    def __init__(self):
        """
        Initialize the controller.
        """
        self.__timersData = defaultdict(dict)  # A dictionary to store timers data for each death zone
        self.__timeToStrikeInCurrentNotification = None  # The time to strike in the current notification
        self.__playerEnterZone = False  # A flag to track whether the player has entered a death zone

    def startControl(self, battleCtx, arenaVisitor):
        """
        Implement the IArenaLoadController interface.
        """
        pass

    def stopControl(self):
        """
        Implement the IArenaLoadController interface.
        """
        pass

    def getControllerID(self):
        """
        Implement the IArenaLoadController interface.
        """
        return BATTLE_CTRL_ID.DEATHZONES

    def updateDeathZoneWarningNotification(self, zoneId, show, timeToStrike, waveDuration):
        """
        Update the death zone warning notification based on the given parameters.

        :param zoneId: The ID of the death zone.
        :param show: A boolean indicating whether to show the notification.
        :param timeToStrike: The time to strike in seconds.
        :param waveDuration: The duration of the wave in seconds.
        """
        if show:
            self.__timersData[zoneId].update({'timeToStrike': timeToStrike, 'waveDuration': waveDuration})
        elif zoneId in self.__timersData:
            self.__timersData.pop(zoneId)
        
        player = BigWorld.player()
        if player is None:
            return
        else:
            if self.__timersData:
                closestStrikeData = min(self.__timersData.values(), key=lambda timersData: timersData['timeToStrike'])
                if closestStrikeData['timeToStrike'] != self.__timeToStrikeInCurrentNotification:
                    player.updateDeathZoneWarningNotification(True, not self.__playerEnterZone, closestStrikeData['timeToStrike'], closestStrikeData['waveDuration'])
                    self.__timeToStrikeInCurrentNotification = closestStrikeData['timeToStrike']
                self.__playerEnterZone = True
            else:
                player.updateDeathZoneWarningNotification(False, False, 0, 0)
                self.__timeToStrikeInCurrentNotification = None
                self.__playerEnterZone =
