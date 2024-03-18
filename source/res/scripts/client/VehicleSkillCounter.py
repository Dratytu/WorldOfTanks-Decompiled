# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/VehicleSkillCounter.py

# Import the DynamicScriptComponent class from the script_component module
from script_component.DynamicScriptComponent import DynamicScriptComponent

# Define the VehicleSkillCounter class that inherits from DynamicScriptComponent
class VehicleSkillCounter(DynamicScriptComponent):

    # Define the set_counterValue method that takes one argument, prev
    def set_counterValue(self, prev):
        # Check if the avatar is ready
        if self._isAvatarReady:
            # Call the private __updateCounter method
            self.__updateCounter()

    # Define the _onAvatarReady method
    def _onAvatarReady(self):
        # Call the private __updateCounter method
        self.__updateCounter()

    # Define the private __updateCounter method
    def __updateCounter(self):
        # Import the g_eventBus, events, and EVENT_BUS_SCOPE from the gui.shared module
        from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
        # Handle the RoleSkillEvent event with the COUNTER_CHANGED action and the updated counter value
        g_eventBus.handleEvent(events.RoleSkillEvent(events.RoleSkillEvent.COUNTER_CHANGED, {'value': self.counterValue}), scope=EVENT_BUS_SCOPE.BATTLE)
