class ToolTipInfo(object):
    """
    Class to hold tooltip information.

    Attributes:
        component (Component): The component associated with the tooltip.
        templateName (str): The name of the tooltip template.
        infoDictionary (dict): A dictionary of keys and values to display in the tooltip.
        infoArea (tuple): A tuple of x, y coordinates representing the area of the component to display the tooltip.
        delayType (int): The delay type for the tooltip (immediate or delayed).
        placement (str): The placement of the tooltip (above, below, left, or right).
    """


class ToolTip(Window):
    """
    Class to represent a tooltip window.

    Attributes:
        items (list): A list of items to display in the tooltip.

    Methods:
        setupToolTip(self, toolTipInfo, infoArea):
            Sets up the tooltip with the given information.

        onSave(self, dataSection):
            Saves the tooltip information to a data section.

        onLoad(self, dataSection):
            Loads the tooltip information from a data section.

        doLayout(self, parent):
            Positions the tooltip on the screen.

        getToolTipPosition(self, mousePos, infoArea, placement):
            Calculates the position of the tooltip on the screen.
    """


class ToolTipManager(object):
    """
    Class to manage tooltips for a given root GUI and z-order.

    Attributes:
        rootGUI (GUI): The root GUI for the tooltips.
        toolTipZOrder (int): The z-order for the tooltips.
        toolTipGUIs (dict): A dictionary of tooltip templates.
        toolTipGUI (GUI): The current tooltip being displayed.
        infoAreaTop (float): The top y-coordinate of the info area.
        infoAreaLeft (float): The left x-coordinate of the info area.
        infoAreaBottom (float): The bottom y-coordinate of the info area.
        infoAreaRight (float): The right x-coordinate of the info area.
        showToolTipCallback (callable): A callback function to show the tooltip.

    Methods:
        addToolTipTemplate(self, templateName, guiFileName):
            Adds a tooltip template to the manager.

        setupToolTip(self, component, toolTipInfo):
            Sets up the tooltip for the given component and information.

        handleMouseEvent(self, event):
            Handles mouse events for the tooltip manager.

        _showToolTip(self, component, toolTipInfo):
            Shows the tooltip for the given component and information.
    """
