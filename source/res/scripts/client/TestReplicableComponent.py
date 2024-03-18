# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/TestReplicableComponent.py

# Import necessary modules and libraries
import BigWorld # For creating DynamicScriptComponent
import CGF # For creating ComponentManager
import GenericComponents # For working with GenericComponents
import GameplayDebug # For working with DebugTextComponent
import cgf_demo.test_replicable # For importing TestReplicableComponent
from cgf_script.managers_registrator import onAddedQuery, onProcessQuery # For event handling

# Define TestReplicableComponent class that inherits from BigWorld.DynamicScriptComponent and cgf_demo.test_replicable.TestReplicableComponent
class TestReplicableComponent(BigWorld.DynamicScriptComponent, cgf_demo.test_replicable.TestReplicableComponent):
    pass

# Define DisplayReplicableValuesManager class that inherits from CGF.ComponentManager
class DisplayReplicableValuesManager(CGF.ComponentManager):

    # Initialize the manager with totalReplicationCount set to 0
    def __init__(self):
        super(DisplayReplicableValuesManager, self).__init__()
        self.totalReplicationCount = 0

    # onAddedQuery decorator for connecting onReplicated event of TestReplicableComponent
    @onAddedQuery(TestReplicableComponent, CGF.GameObject)
    def onAddedType(self, r, go):
        # Connect the __onReplicationDone method to the onReplicated event of r (TestReplicableComponent)
        r.onReplicated += self.__onReplicationDone
        # Remove DynamicModelComponent from the game object if it exists
        go.removeComponentByType(GenericComponents.DynamicModelComponent)
        # If the assetIndex of r is less than the length of r.assets, create a DynamicModelComponent and set its model to r.assets[r.assetIndex]
        if r.assetIndex < len(r.assets):
            go.createComponent(GenericComponents.DynamicModelComponent, r.assets[r.assetIndex])

    # onProcessQuery decorator for displaying replicable values on DebugTextComponent
    @onProcessQuery(TestReplicableComponent, GameplayDebug.DebugTextComponent)
    def displayValues(self, r, text):
        # Display total replication count
        text.addFrameText('Total Replication Count: {0}'.format(self.totalReplicationCount))
        # Display replicableInt value
        text.addFrameText('int: {0}'.format(r.replicableInt
