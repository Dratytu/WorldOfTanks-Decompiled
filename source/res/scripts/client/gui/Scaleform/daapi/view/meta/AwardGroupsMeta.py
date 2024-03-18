# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AwardGroupsMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent  # Importing BaseDAAPIComponent for inheritance

class AwardGroupsMeta(BaseDAAPIComponent):
    # AwardGroupsMeta class inherits from BaseDAAPIComponent
    # This class is a part of the DAAPI (Dynamic Application Programming Interface) system
    # It is used to create and manage Scaleform-based user interfaces in World of Tanks

    def showGroup(self, groupId):
        # This method is used to show a specific group
        # The group to be shown is determined by the input parameter 'groupId'
        self._printOverrideError('showGroup')
        # This line raises a 'NotImplementedError' if the method 'showGroup' is overridden
        # It ensures that the method is not modified without proper implementation

    def as_setDataS(self, groups):
        # This method is used to set data for the AwardGroups component
        # The data is passed as an input parameter 'groups'
        return self.flashObject.as_setData(groups) if self._isDAAPIInited() else None
        # The method returns the result of the 'as_setData' method of the 'flashObject'
        # The '_isDAAPIInited' method is used to check if the DAAPI system is initialized
        # If it's not initialized, the method returns 'None'

    def as_setTooltipsS(self, tooltips):
        # This method is used to set tooltips for the AwardGroups component
        # The tooltips are passed as an input parameter 'tooltips'
        return self.flashObject.as_setTooltips(tooltips) if self._isDAAPIInited() else None
        # The method returns the result of the 'as_setTooltips' method of the 'flashObject'
        # The '_isDAAPIInited' method is used to check if
