# Python bytecode 2.7 (decompiled from Python 2.7)

# Import necessary modules
import functools
import CGF
import Triggers
import Physics

# Import custom modules
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery

@registerComponent # Decorator to register the TestEntranceSpawner class as a component
class TestEntranceSpawner(object):
    # Component properties
    category = DEMO_CATEGORY # The category of the component
    domain = CGF.DomainOption.DomainClient # The domain of the component
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent) # The area trigger to subscribe to
    debrisSpawner = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Spawner to subscribe', value=Physics.PhysicalDebrisSpawnerComponent) # The debris spawner to subscribe to

class EntranceSpawnerManager(CGF.ComponentManager):

    @onAddedQuery(TestEntranceSpawner) # Decorator to register the onEntranceAdded method to be called when a TestEntranceSpawner is added
    def onEntranceAdded(self, entrance):
        trigger = entrance.trigger() # Get the area trigger from the entrance
        if trigger:
            # Add enter and exit reactions to the trigger
            trigger.addEnterReaction(functools.partial(self.__onEnter, entrance))
            trigger.addExitReaction(functools.partial(self.__onExit, entrance))

    def __onEnter(self, entrance, who, where):
        spawner = entrance.debrisSpawner() # Get the debris spawner from the entrance
        if spawner:
            # Spawn debris when an entity enters the trigger area
            spawner.spawnDebris(True)

    def __onExit(self, entrance, who, where):
        spawner = entrance.debrisSpawner() # Get the debris spawner from the entrance
        if spawner:
            # Remove debris when an entity exits the trigger area
            spawner.removeDebris()

