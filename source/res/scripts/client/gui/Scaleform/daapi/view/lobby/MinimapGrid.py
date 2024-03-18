# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.py

import weakref
from gui.Scaleform.daapi.view.meta.MinimapGridMeta import MinimapGridMeta
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class MinimapGrid(MinimapGridMeta):
    """
    The MinimapGrid class is responsible for managing the minimap grid in the lobby.
    It handles controller interactions, map ID changes, and adding commands to the grid.
    """
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        """
        Initialize the MinimapGrid instance.
        """
        super(MinimapGrid, self).__init__()
        self._channel = None  # Reference to the communication channel
        self._controller = None  # Reference to the controller
        self.__mapId = 0  # The current map ID

    def setController(self, controller):
        """
        Set the controller for the minimap grid and activate it.
        :param controller: The controller to be set
        """
        controller.activate()
        self._controller = weakref.ref(controller)

    def removeController(self):
        """
        Remove the controller reference.
        """
        self._controller = lambda : None

    def setActive(self, active):
        """
        Enable or disable clicking on the minimap grid.
        :param active: True to enable clicking, False to disable
        """
        self.as_clickEnabledS(active)

    def setClick(self, x, y):
        """
        Send a command to the controller when the minimap grid is clicked.
        :param x: The x-coordinate of the click
        :param y: The y-coordinate of the click
        """
        controller = self._controller()
        if controller:
            command = controller.proto.unitChat.createByMapPos(x, y)
            controller.sendCommand(command)

    def setMapId(self, mapId):
        """
        Set the current map ID and clear the existing points if the map ID has changed.
        :param
