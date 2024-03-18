# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/ArenaInfoAbilityNotifier.py

import functools
import BigWorld
import CGF
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from items import vehicles
import GenericComponents
from skeletons.gui.battle_session import IBattleSessionProvider

# ArenaInfoAbilityNotifier class inherits from BigWorld.DynamicScriptComponent and CallbackDelayer
class ArenaInfoAbilityNotifier(BigWorld.DynamicScriptComponent, CallbackDelayer):
    # Dependency injection for IBattleSessionProvider
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        # CallbackDelayer initialization
        CallbackDelayer.__init__(self)

    def onLeaveWorld(self, *args):
        # Destroy the component when leaving the world
        self.destroy()

    def notifyLaunchPosition(self, equipmentId, position, launchTime, duration):
        # Calculate delay between current time and launch time
        delay = launchTime - BigWorld.serverTime()
        # Get the equipment object by its ID
        equipment = vehicles.g_cache.equipments()[equipmentId]
        # Show a GUI marker for the equipment at the given position after the calculated delay
        self.__showGuiMarker(equipment, position, delay)
        # Delay the callback for the calculated delay and launch the equipment at the given position with the given duration
        self.delayCallback(delay, functools.partial(self.__launch, equipment, position, duration))

    def __showGuiMarker(self, equipment, position, delay):
        # Get the equipment controller from the shared gui session
        ctrl = self.__guiSessionProvider.shared.equipments
        # If the controller is available
        if ctrl is not None:
            # Show the marker for the equipment at the given position with RGB (0, 0, 0) color and the calculated delay
            ctrl.showMarker(equipment, position, (0, 0, 0), delay)
        return

    def __launch(self, equipment, position, duration):
        # Define a postload setup function for the game object
        def postloadSetup(go):
            # Add the equipment component to the game object
            go.addComponent(equipment)
            # Create a RemoveGoDelayedComponent for the game object with the given duration
            go.createComponent(GenericComponents.RemoveGoDelayed
