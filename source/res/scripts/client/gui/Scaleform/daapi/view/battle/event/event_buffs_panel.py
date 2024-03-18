# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_buffs_panel.py

# Import the EventBuffsPanelMeta class from the gui.Scaleform.daapi.view.meta module.
# This class is the meta class for the EventBuffsPanel view component.
from gui.Scaleform.daapi.view.meta.EventBuffsPanelMeta import EventBuffsPanelMeta

# Define the EventBuffsPanel class, which inherits from the EventBuffsPanelMeta class.
class EventBuffsPanel(EventBuffsPanelMeta):

    # Define the addBuffSlotS method, which takes three arguments:
    #   - idx: an integer representing the index of the buff slot
    #   - imageName: a string representing the name of the buff image
    #   - tooltipText: a string representing the tooltip text for the buff
    def addBuffSlotS(self, idx, imageName, tooltipText):
        # Call the as_addBuffSlotS method on the view component, passing in the three arguments
        self.as_addBuffSlotS(idx, imageName, tooltipText)

    # Define the removeBuffSlotS method, which takes one argument:
    #   - idx: an integer representing the index of the buff slot to remove
    def removeBuffSlotS(self, idx):
        # Call the as_removeBuffSlotS method on the view component, passing in the index of the buff slot to remove
        self.as_removeBuffSlotS(idx)

