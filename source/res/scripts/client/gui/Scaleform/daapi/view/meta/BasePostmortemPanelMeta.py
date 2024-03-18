# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BasePostmortemPanelMeta.py

import sys
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent # Importing BaseDAAPIComponent from the gui.Scaleform.framework.entities module

class BasePostmortemPanelMeta(BaseDAAPIComponent):

    def as_setDeadReasonInfoS(self, reason, showVehicle, vehicleLevel, vehicleImg, vehicleType, vehicleName, userVO):
        """
        :param reason: Reason for the player's death
        :type reason: str
        :param showVehicle: Flag indicating whether the vehicle should be shown
        :type showVehicle: bool
        :param vehicleLevel: Vehicle level
        :type vehicleLevel: int
        :param vehicleImg: Vehicle image
        :type vehicleImg: str
        :param vehicleType: Vehicle type
        :type vehicleType: str
        :param vehicleName: Vehicle name
        :type vehicleName: str
        :param userVO: User voice over
        :type userVO: dict
        :return: Trigger the 'setDeadReasonInfo' event on the client
        :rtype: None
        """
        return self.flashObject.as_setDeadReasonInfo(reason, showVehicle, vehicleLevel, vehicleImg, vehicleType, vehicleName, userVO) if self._isDAAPIInited() else None # Call the 'as_setDeadReasonInfo' method on the flashObject if DAAPI is initialized, otherwise return None

