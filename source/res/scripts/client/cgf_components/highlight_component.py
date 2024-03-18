# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_components/highlight_component.py

import BigWorld  # Import the BigWorld module for working with the game world
import CGF  # Import the CGF module for working with component-based game objects
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery  # Import decorators for handling component additions and removals
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent  # Import tools for defining and registering components
from GenericComponents import DynamicModelComponent  # Import the DynamicModelComponent
from hover_component import IsHoveredComponent  # Import the IsHoveredComponent

# Define the IsHighlighted component
@registerComponent
class IsHighlighted(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor

# Define the HighlightComponent component
@registerComponent
class HighlightComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Highlight'
    category = 'Common'
    color = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName='Color', value=(0, 0, 0, 1), annotations={'colorPicker': {'255Range': False,
                     'useAlpha': True}})
    groupName = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Group name')

# Define the HighlightManager class
class HighlightManager(CGF.ComponentManager):

    # onHoverAdded handles the addition of an IsHoveredComponent to a game object
    @onAddedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverAdded(self, _, gameObject):
        gameObject.createComponent(IsHighlighted)  # Create an IsHighlighted component for the game object

    # onHoverRemoved handles the removal of an IsHoveredComponent from a game object
    @onRemovedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverRemoved(self, _, gameObject):
        gameObject.removeComponentByType(IsHighlighted)  # Remove the IsHighlighted component from the game object

    # onDynamicModelHighlightAdded handles the addition of an IsHighlighted and HighlightComponent to a game object with a DynamicModelComponent
    @onAddedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightAdded(self, _, highlightComponent, dynamicModelComponent):
        BigWorld.wgSetEdgeDetectEdgeColor(3, highlightComponent.color)  # Set the edge detect color for the dynamic model
        BigWorld.wgAddEdgeDetectDynamicModel(dynamicModelComponent)  # Add the dynamic model to edge detect
        self.__enableGroupDraw(True, highlightComponent.groupName)  # Enable drawing for the highlightComponent's group

    # onDynamicModelHighlightRemoved handles the removal of an IsHighlighted and HighlightComponent from a game object with a DynamicModelComponent
    @onRemovedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightRemoved(self, _, highlightComponent, dynamicModelComponent):
        BigWorld.wgDelEdgeDetectDynamicModel(dynamicModelComponent)  # Remove the dynamic model from edge detect
        self.__enableGroupDraw(False, highlightComponent.groupName)  # Disable drawing for the highlightComponent's group

    # onHighlightComponentRemoved handles the removal of a HighlightComponent from a game object with a DynamicModelComponent
    @onRemovedQuery(HighlightComponent, DynamicModelComponent)
    def onHighlightComponentRemoved(self, _, dynamicModelComponent):
        BigWorld.wgDelEdgeDetectDynamicModel(dynamicModelComponent)  # Remove the dynamic model from edge detect

    # __enableGroupDraw enables or disables drawing for a group of highlight components
    def __enableGroupDraw(self, enable, groupName):
        highlightQuery = CGF.Query(self.spaceID, (HighlightComponent, DynamicModelComponent))  # Query for HighlightComponents and DynamicModelComponents
        for highlightComponent, dynamicModelComponent in highlightQuery:  # Iterate through the query results
            if highlightComponent.groupName and highlightComponent.groupName == groupName:  # If the highlightComponent has a group name and it matches the input groupName
                if enable:  # If enable is True
                    BigWorld.wgAddEdge
