# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCTechTree.py

# Import necessary modules
from CurrentVehicle import g_currentVehicle
from bootcamp.Bootcamp import g_bootcamp
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_STATE
from gui.Scaleform.daapi.view.lobby.techtree.techtree_page import TechTree
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS
from gui.shared import event_dispatcher as shared_events, events
from nations import NAMES as NATION_NAMES

# Define the BCTechTree class that inherits from TechTree class
class BCTechTree(TechTree):

    # Define the invalidateBlueprintMode method
    def invalidateBlueprintMode(self, isEnabled):
        # This method does not contain any code
        pass

    # Define the goToNextVehicle method
    def goToNextVehicle(self, vehCD):
        # Check if the research is not free in the current lesson
        if not g_bootcamp.isResearchFreeLesson():
            # Get the nation data
            nationData = g_bootcamp.getNationData()
            # Get the vehicle object
            vehicle = self._itemsCache.items.getItemByCD(int(vehCD))
            # Create an exit event
            exitEvent = events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_TECHTREE), ctx={'nation': vehicle.nationName})
            # Check if the second vehicle in the nation data is equal to the provided vehicle CD
            if nationData['vehicle_second'] == vehCD:
                # Check if the vehicle is in the inventory
                if vehicle.isInInventory:
                    # Show the research view with the provided vehicle CD and the exit event
                    shared_events.showResearchView(vehCD, exitEvent=exitEvent)
                    return
            # Check if the first vehicle in the nation data is equal to the provided vehicle CD
            if nationData['vehicle_first'] == vehCD:
                # Show the research view with the provided vehicle CD and the exit event
                shared_events.showResearchView(vehCD, exitEvent=exitEvent)
        else:
            # Show the research view with the provided vehicle CD
            shared_events.showResearchView(vehCD)

    # Define the getNationTreeData method
    def getNationTreeData(self, nationName):
        # Get the nation tree data from the superclass method
        data = super(BCTechTree, self).getNationTreeData(NATION_NAMES[g_bootcamp.nation])
        # Get the nodes data from the nation tree data
        dataNodes = data.get('nodes', None)
        # Get the nation data
        nationData = g_bootcamp.getNationData()
        # Check if the nodes data is not None
        if dataNodes is not None:
            # Filter out the nodes with premium state
            dataNodes = [node for node in dataNodes if not NODE_STATE.isPremium(node['state'])]
            # Iterate over the nodes data
            for node in dataNodes:
                # Check if the node contains 'vehCompareTreeNodeData' key
                if 'vehCompareTreeNodeData' in node:
                    # Set the 'modeAvailable' key to False
                    node['vehCompareTreeNodeData']['modeAvailable'] = False
                # Get the node state
                nodeState = node['state']
                # Check if the node state is not in the inventory
                if not NODE_STATE.inInventory(nodeState):
                    # Check if the node state is unlocked
                    isUnlocked = NODE_STATE.isUnlocked(nodeState)
                    # Check if the node ID is equal to the second vehicle in the nation data
                    isVehicleSecond = node['id'] == nationData['vehicle_second']
                    # Check if the node is not the second vehicle and is unlocked
                    if not (isVehicleSecond and isUnlocked):
                        # Set the node state to LOCKED
                        node['state'] = NODE_STATE_FLAGS.LOCKED
                    # Check if the node state is unlocked
                    if isUnlocked:
                        # Set the node state to PURCHASE_DISABLED
                        node['state'] |= NODE_STATE_FLAGS.PURCHASE_DISABLED
                    # Check if the node is the second vehicle
                    if isVehicleSecond:
                        # Set the node state to NEXT_2_UNLOCK
                        node['state'] |= NODE_STATE_FLAGS.NEXT_2_UNLOCK
                    # Check if the node state is an announcement
                    if NODE_STATE.isAnnouncement(nodeState):
                        # Set the node state to ANNOUNCEMENT and NOT_CLICKABLE
                        node['state'] |= NODE_STATE_FLAGS.ANNOUNCEMENT
                        node['state'] |= NODE_STATE_FLAGS.NOT_CLICKABLE

            # Set the nodes data in the nation tree data
            data['nodes'] = dataNodes
        # Set the scroll index in the nation tree data
        data['scrollIndex'] = next((i for i, item in enumerate(dataNodes) if item['id'] == g_currentV
