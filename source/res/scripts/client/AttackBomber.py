# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AttackBomber.py

import math
import BigWorld
import Math
from AreaOfEffect import AreaOfEffect
from constants import SERVER_TICK_LENGTH
from items import vehicles

# Class representing an attack bomber with carpet bombing capability
class AttackBomber(AreaOfEffect):
    SKIP_FLAGS = 18
    STRIKE_LINES = (-1, 1)
    LINE_WIDTH = 5.0

    def __init__(self):
        super(AttackBomber, self).__init__()
        self._attackCallbackId = None  # Callback ID for the attack
        return

    def onEnterWorld(self, prereqs):
        super(AttackBomber, self).onEnterWorld(prereqs)
        self._attackCallbackId = BigWorld.callback(self._equipment.delay, self._carpetBombing)

    def onLeaveWorld(self):
        if self._attackCallbackId:
            BigWorld.cancelCallback(self._attackCallbackId)
        super(AttackBomber, self).onLeaveWorld()

    def _carpetBombing(self):
        self._attackCallbackId = None
        equipment = self._equipment  # Equipment data
        effectIndex = vehicles.g_cache.shotEffectsIndexes[equipment.shotEffect]
        shotEffect = vehicles.g_cache.shotEffects[effectIndex]
        airstrikeID = shotEffect.get('airstrikeID')  # Airstrike ID
        if airstrikeID is None:
            return
        else:
            flatDir = Math.Vector3(math.sin(self.yaw), 0, math.cos(self.yaw))  # Flat direction vector
            areaLength = equipment.areaLength  # Area length
            startPoint = self.position - flatDir * areaLength * 0.5  # Start point of the area
            altitude = Math.Vector3(0, self.SHOT_HEIGHT, 0)  # Altitude vector
            collisionPoint = BigWorld.wg_collideSegment(self.spaceID, startPoint + altitude, startPoint - altitude, self.SKIP_FLAGS)
            if collisionPoint is None:
                return
            beginExplosionPos = collisionPoint.closestPoint  # Begin explosion position
            velocity = flatDir * areaLength / max(SERVER_TICK_LENGTH, equipment.duration)  # Velocity
            lateral = flatDir * Math.Vector3(0, 1, 0) * self.LINE_WIDTH  # Lateral vector
            bombsPerLength = int(math.ceil(float(equipment.shotsNumber) / len(self.STRIKE_LINES)))  # Bombs per length
            if bombsPerLength == 1:
                beginExplosionPos = beginExplosionPos + flatDir * (areaLength / 2)
            for line in self.STRIKE_LINES:
                BigWorld.PyGroundEffectManager().playAirstrike(airstrikeID, beginExplosionPos + lateral * line, velocity, self.LINE_WIDTH, areaLength, 1, bombsPerLength * 2)

            return

