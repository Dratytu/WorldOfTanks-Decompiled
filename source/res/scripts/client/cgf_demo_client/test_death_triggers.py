# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_demo_client/test_death_triggers.py

import logging
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery
from cgf_demo.demo_category import DEMO_CATEGORY
import CGF
import functools

# Import the DeathComponent from HealthComponents
from HealthComponents import DeathComponent

# Import the AreaTriggerComponent from Triggers
from Triggers import AreaTriggerComponent

_logger = logging.getLogger(__name__)

# Register the TestAddDeathByTrigger component
@registerComponent
class TestAddDeathByTrigger(object):
    # Set the category and domain of the component
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    
    # Define the goLink property with the specified type, editor name, and default value
    goLink = ComponentProperty(type=CGFMetaTypes.LINK, editorName='goLink', value=CGF.GameObject)

# Register the TestRemoveDeathByTrigger component
@registerComponent
class TestRemoveDeathByTrigger(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    goLink = ComponentProperty(type=CGFMetaTypes.LINK, editorName='goLink', value=CGF.GameObject)

# Define the TestDeathByTriggerManager component
@autoregister(presentInAllWorlds=True, category=DEMO_CATEGORY)
class TestDeathByTriggerManager(CGF.ComponentManager):

    # Define the onAddedAddDeath method, which is called when a GameObject with an AreaTriggerComponent and a TestAddDeathByTrigger component is added
    @onAddedQuery(CGF.GameObject, AreaTriggerComponent, TestAddDeathByTrigger)
    def onAddedAddDeath(self, go, trigger, addDeath):
        # Add an enter reaction to the trigger, which calls the __addDeath method with the goLink of the TestAddDeathByTrigger component
        trigger.addEnterReaction(functools.partial(self.__addDeath, addDeath.goLink))

    # Define the onAddedRemoveDeath method, which is called when a GameObject with an AreaTriggerComponent and a TestRemoveDeathByTrigger component is added
    @onAddedQuery(CGF.GameObject, AreaTriggerComponent, TestRemoveDeathByTrigger)
    def onAddedRemoveDeath(self, go, trigger, removeDeath):
        # Add an enter reaction to the trigger, which calls the __removeDeath method with the goLink of the TestRemoveDeathByTrigger component
        trigger.addEnterReaction(functools.partial(self.__removeDeath, removeDeath.goLink))

    # Define the __addDeath method,
