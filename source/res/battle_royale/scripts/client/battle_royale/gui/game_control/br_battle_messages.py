# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/br_battle_messages.py

# Import necessary modules and libraries
import BigWorld
from helpers import dependency
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener
from skeletons.gui.battle_session import IBattleSessionProvider
import BattleReplay

# Define the ProgressionMessagesPlayer class that inherits from IProgressionListener
class ProgressionMessagesPlayer(IProgressionListener):
    # Use dependency injection to get an instance of IBattleSessionProvider
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def updateData(self, arenaLevelData):
        # Check if the replay is playing and time warp is in progress
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            # If yes, return and do not execute the rest of the function
            return
        # Check if the arena level is 1 or if the level has not been changed
        elif arenaLevelData.level == 1 or not arenaLevelData.levelIsChanged:
            # If yes, return and do not execute the rest of the function
            return
        else:
            # Get the messages controller
            ctrl = self._sessionProvider.shared.messages
            # Check if the player is an observer
            isObserver = BigWorld.player().isObserver()
            # Check if the messages controller exists and the player is not an observer
            if ctrl is not None and not isObserver:
                # If yes, show the player message with the key 'VEHICLE_LEVEL_UP' and the level in Roman numerals
                ctrl.onShowPlayerMessageByKey('VEHICLE_LEVEL_UP', {'level': int2roman(arenaLevelData.level)})
            # Return after showing the message
            return

    def onMaxLvlAchieved(self):
        # Check if the replay is playing and time warp is in progress
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            # If yes, return and do not execute the rest of the function
            return
        else:
            # Get the messages controller
            ctrl = self._sessionProvider.shared.messages
           
