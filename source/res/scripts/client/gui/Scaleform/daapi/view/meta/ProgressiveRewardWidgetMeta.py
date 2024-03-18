# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProgressiveRewardWidgetMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities import BaseDAAPIComponent

# Define the ProgressiveRewardWidgetMeta class, which inherits from BaseDAAPIComponent
class ProgressiveRewardWidgetMeta(BaseDAAPIComponent):

    # onWidgetClick method is defined, but it only calls the helper method _printOverrideError
    def onWidgetClick(self):
        self._printOverrideError('onWidgetClick')

    # as_setDataS method is defined, which returns the result of the as_setData method called on the flashObject
    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

