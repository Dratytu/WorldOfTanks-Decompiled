# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/AccountBattleRoyaleTournamentComponent.py

import logging
import BigWorld
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleTournamentController
import BattleRoyaleTournament

# Create a logger for this module using the name of the module
_logger = logging.getLogger(__name__)

# Define a class AccountBattleRoyaleTournamentComponent that inherits from BigWorld.StaticScriptComponent
class AccountBattleRoyaleTournamentComponent(BigWorld.StaticScriptComponent):
    # Define a dependency descriptor for IBattleRoyaleTournamentController
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController)

    # Define a method setParticipants that takes a single argument participants
    def setParticipants(self, participants):
        # Log a debug message with the participants
        _logger.debug("got tournament participants: '%r'", participants)
        # Call the updateParticipants method of the battle royale tournament controller
        self.__battleRoyaleTournamentController.updateParticipants(participants)

    # Define a method setTournamentToken that takes a single argument token
    def setTournamentToken(self, token):
        # Log a debug message with the token
        _logger.debug("got joined tournament token: '%r'", token)
        # Call the selectBattleRoyaleTournament method of the battle royale tournament controller
        self.__battleRoyaleTournamentController.selectBattleRoyaleTournament(token)

    # Define a method tournamentJoin that takes three arguments tournamentID, callback (optional)
    def tournamentJoin(self, tournamentID, callback=None):
        # Call the _doCmdIntStr method of the entity with the CMD_BATTLE_ROYALE_TRN_JOIN command, 0, tournamentID, and callback
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_JOIN, 0, tournamentID, callback)

    # Define a method tournamentLeave that takes a single argument callback (optional)
    def tournamentLeave(self, callback=None):
        # Call the _doCmdIntStr method of the entity with the CMD_BATTLE_ROYALE_TRN_LEAVE command, 0, '', and callback
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_LEAVE, 0, '', callback)

    # Define a method tournamentReady that takes three arguments vehInvID, tournamentID, callback (optional)
    def tournamentReady(self, vehInvID, tournamentID, callback=None):
        # Call the _doCmdIntStr method of the entity
