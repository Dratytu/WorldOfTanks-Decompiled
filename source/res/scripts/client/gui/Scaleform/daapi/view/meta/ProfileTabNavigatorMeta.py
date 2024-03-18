# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTabNavigatorMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent # Importing BaseDAAPIComponent class from the Scaleform framework.

class ProfileTabNavigatorMeta(BaseDAAPIComponent):
    """
    Meta class for the ProfileTabNavigator component.
    This class is responsible for handling communication between ActionScript and Python.
    """

    def onTabChange(self, tabId):
        """
        Method called when a tab is changed in the user interface.
        :param tabId: The ID of the tab that was changed.
        """
        self._printOverrideError('onTabChange') # Print an error message if this method is overridden.

    def as_setInitDataS(self, data):
        """
        Method called to set the initial data for the component.
        :param data: A dictionary containing the initial data.
        :return: An ActionScript message containing the initial data.
        """
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None # Return the message if the DAAPI is initialized, otherwise return None.

    def as_setBtnTabCountersS(self, counters):
        """
        Method called to set the button tab counters for the component.
        :param counters: A dictionary containing the button tab counters.
        :return: An ActionScript message containing the button tab counters.
        """
        return self.flashObject.as_setBtnTabCounters(counters) if self._isDAAPIInited() else None # Return the message if the DAAPI is initialized, otherwise return None.

