# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/AvatarBattleRoyaleComponent.py

import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
import BattleReplay
from BattleReplay import g_replayEvents
from Event import EventsSubscriber

# AvatarBattleRoyaleComponent class inherits from BigWorld.DynamicScriptComponent and EventsSubscriber
class AvatarBattleRoyaleComponent(BigWorld.DynamicScriptComponent, EventsSubscriber):
    # Dependency injection for IBattleSessionProvider
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(AvatarBattleRoyaleComponent, self).__init__()

        # Check if the replay is playing and configure resource loading accordingly
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.useSyncroniusResourceLoading(True)
            self.subscribeToEvent(g_replayEvents.onTimeWarpStart, self.__onTimeWarpStart)
            self.subscribeToEvent(g_replayEvents.onTimeWarpFinish, self.__onTimeWarpFinish)

    def onLeaveWorld(self):
        # Unsubscribe from all events when leaving the world
        self.unsubscribeFromAllEvents()

    def set_playerPlace(self, _prev):
        # Set the player's place in the battle royale
        self.sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent.setBattleRoyalePlace(self.playerPlace)

    def set_defeatedTeams(self, _prev):
        # Set the defeated teams in the battle royale
        self.sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent.setDefeatedTeams(self.defeatedTeams)

    def __onTimeWarpStart(self):
        # Disable world drawing when time warp starts
        BigWorld.worldDrawEnabled(False)

    def __onTimeWarpFinish(self):
        # Enable world drawing when time warp finishes
        BigWorld.worldDrawEnabled(True)

