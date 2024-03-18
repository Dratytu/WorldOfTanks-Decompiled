# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PopOverViewMeta.py

import sys
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta  # Importing WrapperViewMeta, as PopOverViewMeta inherits from it

class PopOverViewMeta(WrapperViewMeta):
    """
    The PopOverViewMeta class is a Scaleform view meta class for creating pop-over views.
    It inherits from WrapperViewMeta, which provides basic functionality for Scaleform view components.
    """

    def as_setArrowDirectionS(self, value):
        """
        The as_setArrowDirectionS() method sets the arrow direction of the pop-over view.
        :param value: The arrow direction value
        :return: None if the DAAPI is not initialized, otherwise, it returns the result of the as_setArrowDirection() method called on the flashObject
        """
        return self.flashObject.as_setArrowDirection(value) if self._isDAAPIInited() else None

    def as_setArrowPositionS(self, value):
        """
        The as_setArrowPositionS() method sets the arrow position of the pop-over view.
        :param value: The arrow position value
        :return: None if the DAAPI is not initialized, otherwise, it returns the result of the as_setArrowPosition() method called on the flashObject
        """
        return self.flashObject.as_setArrowPosition(value) if self._isDAAPIInited() else None

