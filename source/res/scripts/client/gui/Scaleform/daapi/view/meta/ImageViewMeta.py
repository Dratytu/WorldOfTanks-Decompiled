# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ImageViewMeta.py

import weakref
from gui.Scaleform.framework.entities.View import View

class ImageViewMeta(View):
    """
    Meta class for the ImageView component.
    This class inherits from the base View class and provides functionality for displaying images.
    """

    def onClose(self):
        """
        Override method for handling the 'onClose' event.
        This method should be implemented in the derived class to handle the event when the view is closed.
        """
        self._printOverrideError('onClose')

    def as_setBgPathS(self, value):
        """
        External method for setting the background path of the image.
        :param value: str - The path of the background image.
        :return: None
        """
        return self.flashObject.as_setBgPath(value) if self._isDAAPIInited() else None

