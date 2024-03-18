# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/controllers/epic_team_bases_ctrl.py

# Import necessary modules
import BigWorld
import BattleReplay
from debug_utils import LOG_ERROR
from epic_constants import EPIC_BATTLE_TEAM_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from team_bases_ctrl import BattleTeamsBasesController, makeClientTeamBaseID

# Define the EpicBattleTeamsBasesController class, which is a subclass of BattleTeamsBasesController
class EpicBattleTeamsBasesController(BattleTeamsBasesController):

    # Dependency injection for the IBattleSessionProvider interface
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Initialize the EpicBattleTeamsBasesController class
    def __init__(self):
        # Initialize the superclass
        super(EpicBattleTeamsBasesController, self).__init__()
        # Initialize instance variables
        self.__capturedBasesDict = {}
        self.__currentBaseID = None
        self.__currentBaseTeam = EPIC_BATTLE_TEAM_ID.TEAM_DEFENDER

    # Method for starting control of team bases
    def startControl(self, battleCtx, arenaVisitor):
        # Start control of team bases in the superclass
        super(EpicBattleTeamsBasesController, self).startControl(battleCtx, arenaVisitor)
        # Get the component system from the arena visitor
        componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
        # Get the player data component from the component system
        playerDataComp = getattr(componentSystem, 'playerDataComponent', None)
        # If the player data component is present, add an event listener for player physical lane updates
        if playerDataComp is not None:
            playerDataComp.onPlayerPhysicalLaneUpdated += self.__onPlayerPhysicalLaneUpdated
        else:
            LOG_ERROR('Expected PlayerDataComponent not present!')
        # Get the sector base component from the component system
        sectorBaseComp = getattr(componentSystem, 'sectorBaseComponent', None)
        # If the sector base component is present, add event listeners for sector base captured and sector base points update events
        if sectorBaseComp is not None:
            sectorBaseComp.onSectorBaseCaptured += self.__onSectorBaseCaptured
            sectorBaseComp.onSectorBasePointsUpdate += self.__onSectorBasePointsUpdate
        else:
            LOG_ERROR('Expected SectorBaseComponent not present!')

    # Method for stopping control of team bases
    def stopControl(self):
        # Get the component system from the arena visitor
        componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
        # Get the player data component from the component system
        playerDataComp = getattr(componentSystem, 'playerDataComponent', None)
        # If the player data component is present, remove the event listener for player physical lane updates
        if playerDataComp is not None:
            playerDataComp.onPlayerPhysicalLaneUpdated -= self.__onPlayerPhysicalLaneUpdated
        # Get the sector base component from the component system
        sectorBaseComp = getattr(componentSystem, 'sectorBaseComponent', None)
        # If the sector base component is present, remove event listeners for sector base captured and sector base points update events
        if sectorBaseComp is not None:
            sectorBaseComp.onSectorBaseCaptured -= self.__onSectorBaseCaptured
            sectorBaseComp.onSectorBasePointsUpdate -= self.__onSectorBasePointsUpdate
        # Stop control of team bases in the superclass
        super(EpicBattleTeamsBasesController, self).stopControl()

    # Method for checking if a team base is empty and not under attack
    def _teamBaseLeft(self, points, invadersCnt):
        # Return True if the points are 0 and the number of invaders is less than 1, otherwise return False
        return not points and invadersCnt < 1

    # Method for updating the points for a team base
    def _updatePoints(self, clientID):
        # If the client ID is not in the controller, return
        if not self._containsClientID(clientID):
            return
        # Get the points, time left timestamp, number of invaders, and capturing stopped status for the client ID
        points, timeLeftTimeStamp, invadersCnt, stopped = self._getPoints(clientID)
        # If capturing has stopped, return
        if stopped:
            return
        # Calculate the time left
        timeLeft = timeLeftTimeStamp - BigWorld.serverTime()
        # Calculate the progress rate
        rate = self._getProgressRate()
        # If there are view components and the snapshot dictionary for the client ID is not the same as the current points, rate, and time left, update the snapshot dictionary and view components
        if self._viewComponents and self._getSnap
