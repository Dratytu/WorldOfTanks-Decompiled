# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/Radar.py

import BigWorld

class Radar(BigWorld.DynamicScriptComponent):
    """
    A class representing the Radar component for a vehicle in the game world.
    Inherits from BigWorld.DynamicScriptComponent.
    """

    def onEnterWorld(self, *args):
        """
        Called when the entity (vehicle) enters the game world.
        """
        pass

    def onLeaveWorld(self, *args):
        """
        Called when the entity (vehicle) leaves the game world.
        """
        pass

    def set_radarReadinessTime(self, _=None):
        """
        Sets the radar readiness time.

        :param _: Unused argument
        """
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadinessTime(self.radarReadinessTime)

    def set_radarReady(self, prev=None):
        """
        Sets the radar readiness state.

        :param prev: Previous radar readiness state
        """
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadiness(self.radarReady)

    def refreshRadar(self):
        """
        Refreshes the radar by updating the radar readiness time and state.
        """
        self.set_radarReadinessTime()
        self.set_radarReady()
