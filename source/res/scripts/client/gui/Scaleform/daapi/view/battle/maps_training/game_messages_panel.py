# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/game_messages_panel.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel, PlayerMessageData
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter  # For getting player team information
from gui.impl import backport  # For localizing strings
from gui.impl.gen import R  # For accessing resource files


class MapsTrainingGameMessagesPanel(GameMessagesPanel):

    def sendEndGameMessage(self, winningTeam, reason, extraData):
        # Determine the message type based on the winning team and whether the player is on the winning team
        messageType = GAME_MESSAGES_CONSTS.DRAW
        if winningTeam != 0:
            isWinner = avatar_getter.getPlayerTeam() == winningTeam
            if isWinner:
                messageType = GAME_MESSAGES_CONSTS.WIN
            else:
                messageType = GAME_MESSAGES_CONSTS.DEFEAT

        # Create end game message data with a localized title based on the message type
        endGameMsgData = {'title': backport.text(R.strings.maps_training.finalBattleScreen.dyn(messageType)())}

        # Create a PlayerMessageData object with the message type, length, priority, and end game message data
        msg = PlayerMessageData(messageType, GAME_MESSAGES_CONSTS.DEFAULT_MESSAGE_LENGTH, GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_END_GAME, endGameMsgData)

        # Add the message to the panel
        self._addMessage(msg.getDict())

