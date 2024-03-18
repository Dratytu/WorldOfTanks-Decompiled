# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/battleground/airdrops.py

# Importing necessary modules and constants
from constants import AirdropType
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from arena_component_system.client_arena_component_system import ClientArenaComponent
from battleground.bot_drop_object import BotAirdrop
from battleground.loot_drop_object import PlaneLootAirdrop

# Defining the Airdrops class
class Airdrops(object):
    # Declaring the dependency for IBattleSessionProvider
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Function to schedule a loot airdrop
    def scheduleLoot(self, dropID, position, serverTime):
        # Creating a new PlaneLootAirdrop object and starting it
        planeObj = PlaneLootAirdrop(dropID, position, serverTime)
        planeObj.start()

    # Function to schedule a bot airdrop
    def scheduleBot(self, dropID, position, teamID, yawAxis, serverTime, airdropType=AirdropType.BOT):
        # Creating a new BotAirdrop object with the given parameters and starting it
        botObj = BotAirdrop(dropID, position, teamID, yawAxis, serverTime, airdropType)
        botObj.start()


# Defining the AirdropsComponent class, which inherits from both ClientArenaComponent and Airdrops
class AirdropsComponent(ClientArenaComponent, Airdrops):

    # Initializing the AirdropsComponent class
    def __init__(self, componentSystem):
        # Calling the constructor of Airdrops
        Airdrops.__init__(self)
        # Calling the constructor of ClientArenaComponent
        ClientArenaComponent.__init__(self, componentSystem)
