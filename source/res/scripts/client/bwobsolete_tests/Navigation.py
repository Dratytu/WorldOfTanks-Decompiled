# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/bwobsolete_tests/Navigation.py

import BigWorld
from bwdebug import * # Import debugging functions

class Navigation:
    DEBUG_MODEL_NAME = 'helpers/models/unit_cube.model' # Debug model name for visualizing navigation path

    # Preload the debug model for performance reasons
    preload = BigWorld.Model(DEBUG_MODEL_NAME)

    def __init__(self):
        """
        Initialize the Navigation class.
        :param self: Navigation instance
        """
        self._player = None # Player entity
        self._debugNavPathModels = [] # List to store debug nav path models

    def __fini__(self):
        """
        Cleanup resources when the Navigation instance is destroyed.
        :param self: Navigation instance
        """
        self.stopTest()

    def testPath(self, player, targetPosition):
        """
        Calculate and display a navigation path between the player and target position.
        :param self: Navigation instance
        :param player: Player entity
        :param targetPosition: Target position as a tuple (x, y, z)
        """
        self._player = player
        self._moveNavPath = self._calculatePath(player.position, targetPosition)
        self._cleanupNavPathModels()
        self._attachDebugModels()

    def stopTest(self):
        """
        Cleanup navigation path models and stop the test.
        :param self: Navigation instance
        """
        self._cleanupNavPathModels()

    def _calculatePath(self, startPosition, targetPosition):
        """
        Calculate the navigation path between startPosition and targetPosition.
        :param self: Navigation instance
        :param startPosition: Starting position as a tuple (x, y, z)
        :param targetPosition: Target position as a tuple (x, y, z)
        :return: List of path points as tuples (x, y, z)
        """
        path = []
        try:
            path = BigWorld.navigatePathPoints(startPosition, targetPosition)
            DEBUG_MSG('start', startPosition) # Debug message: starting position
            DEBUG_MSG('target', targetPosition) # Debug message: target position
            DEBUG_MSG('path', path) # Debug message: navigation path
        except ValueError as e:
            DEBUG_MSG(e) # Debug message: error during path calculation
            DEBUG_MSG('start', startPosition, 'end', targetPosition) # Debug message: starting and ending positions
            path = [startPosition, targetPosition] # If an error occurs, use a straight line between start and end positions

        return path

    def _attachDebugModels(self):
        """
        Attach debug models to each path point for visualization.
        :
