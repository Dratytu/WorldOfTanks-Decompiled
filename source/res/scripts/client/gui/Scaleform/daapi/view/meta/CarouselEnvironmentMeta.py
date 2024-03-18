# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CarouselEnvironmentMeta.py

from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent # Importing BaseDAAPIComponent from the gui.Scaleform.framework.entities module

class CarouselEnvironmentMeta(BaseDAAPIComponent):

    def selectVehicle(self, id):
        """
        Overrides the selectVehicle method from the BaseDAAPIComponent class.
        :param id: The vehicle ID to be selected.
        """
        self._printOverrideError('selectVehicle')

    def resetFilters(self):
        """
        Overrides the resetFilters method from the BaseDAAPIComponent class.
        """
        self._printOverrideError('resetFilters')

    def updateHotFilters(self):
        """
        Overrides the updateHotFilters method from the BaseDAAPIComponent class.
        """
        self._printOverrideError('updateHotFilters')

    def as_getDataProviderS(self):
        """
        Returns the data provider as an action script object if the DAAPI is initialized.
        :return: The action script object representing the data provider.
        """
        return self.flashObject.as_getDataProvider() if self._isDAAPIInited() else None

    def as_setInitDataS(self, data):
        """
        Sets the initial data as an action script object if the DAAPI is initialized.
        :param data: The action script object containing the initial data.
        :return: The action script object representing the result of the operation.
        """
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None

    def as_setEnabledS(self, value):
        """
        Sets the enabled status as an action script object if the DAAPI is initialized.
        :param value: The boolean value indicating whether the component is enabled or not.
        :return: The action script object representing the result of the operation.
        """
        return self.flashObject.as_setEnabled(value) if self._isDAAPIInited() else None

    def as_showCounterS(self, countText, isAttention):
        """
        Shows the counter with the specified count text and attention status as an action script object if the DAAPI is initialized.
        :param countText: The text to be displayed on the counter.
        :param isAttention: The boolean value indicating whether the counter should attract attention or not.
        :return: The action script object representing the result of
