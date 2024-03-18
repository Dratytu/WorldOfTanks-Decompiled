# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/minimap/entries.py

import BigWorld
from gui.Scaleform.daapi.view.battle.shared.minimap import settings
from gui.battle_control.battle_constants import VEHICLE_LOCATION
from gui.shared.utils.decorators import ReprInjector

# A base class for all minimap entries
class MinimapEntry(object):
    __slots__ = ('_entryID', '_isActive', '_matrix')

    def __init__(self, entryID, active, matrix=None):
        """
        Initialize a new MinimapEntry instance.

        :param entryID: The unique identifier of the entry.
        :type entryID: int
        :param active: A boolean indicating whether the entry is active or not.
        :type active: bool
        :param matrix: The transformation matrix for the entry.
        :type matrix: mathtypes.Matrix3D or None
        """
        super(MinimapEntry, self).__init__()
        self._entryID = entryID
        self._isActive = active
        self._matrix = matrix

    def getID(self):
        """
        Get the unique identifier of the entry.

        :return: The unique identifier of the entry.
        :rtype: int
        """
        return self._entryID

    def getMatrix(self):
        """
        Get the transformation matrix for the entry.

        :return: The transformation matrix for the entry.
        :rtype: mathtypes.Matrix3D or None
        """
        return self._matrix

    def setMatrix(self, matrix):
        """
        Set the transformation matrix for the entry.

        :param matrix: The transformation matrix for the entry.
        :type matrix: mathtypes.Matrix3D or None
        :return: True if the matrix was set, False otherwise.
        :rtype: bool
        """
        self._matrix = matrix
        return True

    def isActive(self):
        """
        Get a boolean indicating whether the entry is active or not.

        :return: A boolean indicating whether the entry is active or not.
        :rtype: bool
        """
        return self._isActive

    def setActive(self, active):
        """
        Set the active status of the entry.

        :param active: A boolean indicating whether the entry should be active or not.
        :type active: bool
        :return: True if the active status was changed, False otherwise.
        :rtype: bool
        """
        if self._isActive != active:
            self._isActive = active
            return True
        return False

    def clear(self):
        """
        Clear the entry, resetting all its properties to their default values.
        """
        self._entryID = 0
        self._isActive = False
        self._matrix = None
        return


@ReprInjector.simple(('_entryID', 'id'), ('_isActive', 'active'), ('_isInAoI', 'AoI'), ('_isEnemy', 'enemy'), ('_classTag', 'class'))
class VehicleEntry(MinimapEntry):
    __slots__ = ('_entryID', '_classTag', '_location', '_guiLabel', '_spottedCount', '_spottedTime', '_isInAoI', '_isEnemy', '_isAlive')

    def __init__(self, entryID, active, matrix=None, location=VEHICLE_LOCATION.UNDEFINED):
        """
        Initialize a new VehicleEntry instance.

        :param entryID: The unique identifier of the entry.
        :type entryID: int
        :param active: A boolean indicating whether the entry is active or not.
        :type active: bool
        :param matrix: The transformation matrix for the entry.
        :type matrix: mathtypes.Matrix3D or None
        :param location: The location of the vehicle on the battlefield.
        :type location: VEHICLE_LOCATION or int
        """
        super(VehicleEntry, self).__init__(entryID, active, matrix=matrix)
        self._isInAoI = False
        self._isEnemy = True
        self._classTag = None
        self._guiLabel = ''
        self._isAlive = True
        self._location = location
        if active:
            self._spottedCount = 1
            self._spottedTime = BigWorld.serverTime()
        else:
            self._spottedCount = 0
            self._spottedTime = None
        return

    def isEnemy(self):
        """
        Get a boolean indicating whether the vehicle is an enemy or not.

        :return: A boolean indicating whether the vehicle is an enemy or not.
        :rtype: bool
        """
        return self._isEnemy

    def getClassTag(self):
        """
        Get the class tag of the vehicle.

        :return: The class tag of the vehicle.
        :rtype: str
        """
        return self._classTag

    def setVehicleInfo(self, isEnemy, guiLabel, classTag, isAlive):
        """
        Set the vehicle information.

        :param isEnemy: A boolean indicating whether the vehicle is an enemy or not.
        :type isEnemy: bool
        :param guiLabel: The label of the vehicle for the GUI.
        :type guiLabel: str
        :param classTag: The class tag of the vehicle.
        :type classTag: str
        :param isAlive: A boolean indicating whether the vehicle is alive or not.
        :type isAlive: bool
        :return: True if the vehicle information was changed, False otherwise.
        :rtype: bool
        """
        self._isEnemy = isEnemy
        self._classTag = classTag
        self._guiLabel = guiLabel
        self._isAlive = isAlive
        return True

    def getGUILabel(self):
        """
        Get the label of the vehicle for the GUI
