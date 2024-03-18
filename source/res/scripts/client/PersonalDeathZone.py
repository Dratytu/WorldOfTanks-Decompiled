# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/PersonalDeathZone.py

import BigWorld  # Import the BigWorld module for world-related functionality
import Math  # Import the Math module for vector and matrix math
from AreaOfEffect import AreaOfEffect  # Import AreaOfEffect base class
import TriggersManager  # Import TriggersManager for trigger management

class PersonalDeathZone(AreaOfEffect, TriggersManager.ITriggerListener):
    # PersonalDeathZone class inherits from AreaOfEffect and TriggersManager.ITriggerListener
    _TRIGGER_NAME_TEMPLATE = 'personal_deathzone_{}'  # Trigger name template
    _TRIGGER_EXIT_INTERVAL = 1.0  # Trigger exit interval
    _TRIGGER_SCALE = (1, 1, 1)  # Trigger scale
    _TRIGGER_DIRECTION_AXIS = 1  # Trigger direction axis

    def __init__(self):
        super(PersonalDeathZone, self).__init__()
        self._triggerName = self._TRIGGER_NAME_TEMPLATE.format(self.id)
        self._triggerId = None
        self._triggered = False
        return

    def onEnterWorld(self, prereqs):
        # Called when the entity enters the world
        super(PersonalDeathZone, self).onEnterWorld(prereqs)
        TriggersManager.g_manager.addListener(self)  # Register as a trigger listener
        self._triggerId = TriggersManager.g_manager.addTrigger(
            TriggersManager.TRIGGER_TYPE.AREA,  # Trigger type
            name=self._triggerName,  # Trigger name
            position=self.position,  # Trigger position
            radius=self._equipment.areaRadius,  # Trigger radius
            scale=self._TRIGGER_SCALE,  # Trigger scale
            exitInterval=self._TRIGGER_EXIT_INTERVAL,  # Trigger exit interval
            direction=Math.Matrix(self.matrix).applyToAxis(self._TRIGGER_DIRECTION_AXIS)  # Trigger direction
        )

    def onLeaveWorld(self):
        # Called when the entity leaves the world
        if self._triggered:
            BigWorld.player().updatePersonalDeathZoneWarningNotification(False, 0)
        TriggersManager.g_manager.delListener(self)  # Unregister as a trigger listener
        if self._triggerId is not None:
            TriggersManager.g_manager.delTrigger(self._triggerId)
            self._triggerId = None
        super(PersonalDeathZone, self).onLeaveWorld()
        return

    def onTriggerActivated(self, args):
        # Called when a trigger is activated
        if args['type'] == TriggersManager.TRIGGER_TYPE.AREA and args['name'] == self._triggerName:
            self._triggered = True
            BigWorld.player().updatePersonalDeathZoneWarningNotification(True, self.strikeTime)

    def onTriggerDeactivated(self, args):
        # Called when a trigger is deactivated
        if args['type'] == TriggersManager.TRIGGER_TYPE.AREA and args['name'] == self._triggerName:
            self._
