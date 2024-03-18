# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsVehicleSelectorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsVehicleSelectorMeta(BaseDAAPIComponent):
    """
    The MissionsVehicleSelectorMeta class is a Scaleform-based view component for displaying and managing a list of vehicles
    in the context of missions or other in-game events. It provides methods for initializing the component with data,
    showing a selected vehicle, hiding the selected vehicle, and closing the component.
    """

    def as_setInitDataS(self, data):
        """
        Sets the initial data for the vehicle selector component.

        :param data: A dictionary containing the initial data for the component.
        :return: A ActionScript message to be sent to the Scaleform SWF.
        """
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None

    def as_showSelectedVehicleS(self, vehData):
        """
        Displays the data for a selected vehicle in the vehicle selector component.

        :param vehData: A dictionary containing the data for the selected vehicle.
        :return: A ActionScript message to be sent to the Scaleform SWF.
        """
        return self.flashObject.as_showSelectedVehicle(vehData) if self._isDAAPIInited() else None

    def as_hideSelectedVehicleS(self):
        """
        Hides the currently selected vehicle in the vehicle selector component.

        :return: A ActionScript message to be sent to the Scaleform SWF.
        """
        return self.flashObject.as_hideSelectedVehicle() if self._isDAAPIInited() else None

    def as_closeS(self):
        """
        Closes the vehicle selector component.

        :return: A ActionScript message to be sent to the Scaleform SWF.

