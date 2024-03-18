# Python bytecode 2.7 (decompiled from Python 2.7)

# Import necessary modules
import CGF
import Event
from GenericComponents import VSEComponent
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery

# Define the TriggerVSEComponent class
@registerComponent  # Register the component with CGF
class TriggerVSEComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor  # Define the domain for the component
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, editorName='event name', value='event')  # Define a property for the event name

    def __init__(self):
        super(TriggerVSEComponent, self).__init__()  # Initialize the superclass
        self.triggerEvent = Event.Event()  # Create an Event object


# Define the TriggerVSEComponentsManager class
class TriggerVSEComponentsManager(CGF.ComponentManager):

    # Define a method to handle component added
    @onAddedQuery(TriggerVSEComponent, VSEComponent)
    def handleComponentAdded(self, triggerVseComponent, vseComponent):
        triggerVseComponent.triggerEvent += vseComponent.context.onTriggerEvent  # Connect the triggerEvent to the onTriggerEvent of the VSEComponent

    # Define a method to handle component removed
    @onRemovedQuery(TriggerVSEComponent, VSEComponent)
    def handleComponentRemoved(self, triggerVseComponent, vseComponent):
        triggerVseComponent.triggerEvent -= vseComponent.context.onTriggerEvent  # Disconnect the triggerEvent from the onTriggerEvent of the VSEComponent
