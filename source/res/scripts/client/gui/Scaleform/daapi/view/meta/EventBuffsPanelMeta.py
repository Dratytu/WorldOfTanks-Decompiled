# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBuffsPanelMeta.py

import sys
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent # Importing BaseDAAPIComponent from the gui.Scaleform.framework.entities module

class EventBuffsPanelMeta(BaseDAAPIComponent):

    def as_addBuffSlotS(self, idx, imageName, tooltipText):
        """
        :param idx: Index of the buff slot to be added.
        :param imageName: Name of the image for the buff slot.
        :param tooltipText: Tooltip text for the buff slot.
        :return: Returns the result of invoking as_addBuffSlot on the flashObject if DAAPI is initialized, otherwise None.
        """
        return self.flashObject.as_addBuffSlot(idx, imageName, tooltipText) if self._isDAAPIInited() else None

    def as_removeBuffSlotS(self, idx):
        """
        :param idx: Index of the buff slot to be removed.
        :return: Returns the result of invoking as_removeBuffSlot on the flashObject if DAAPI is initialized, otherwise None.
        """
        return self.flashObject.as_removeBuffSlot(idx) if self._isDAAPIInited() else None

