# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCTooltipsWindowMeta.py

import sys # Imported, but not used in the code
from gui.Scaleform.framework.entities.View import View # Inherited from View class

class BCTooltipsWindowMeta(View):
    """
    A meta class for the BCTooltipsWindow, which is a view for displaying tooltips in the game.
    """

    def animFinish(self):
        """
        A method that calls the _printOverrideError method with the argument 'animFinish'.
        This method is intended to be overridden in a subclass.
        """
        self._printOverrideError('animFinish')

    def as_setRotateTipVisibilityS(self, Visible):
        """
        A method that returns the result of as_setRotateTipVisibility(Visible) method call on the flashObject.
        This method is used for setting the visibility of the rotate tip.

        :param Visible: A boolean value indicating whether the rotate tip should be visible or not.
        :return: None
        """
        return self.flashObject.as_setRotateTipVisibility(Visible) if self._isDAAPIInited() else None

    def as_showHandlerS(self):
        """
        A method that returns the result of as_showHandler() method call on the flashObject.
        This method is used for showing the tooltip.

        :return: None
        """
        return self.flashObject.as_showHandler() if self._isDAAPIInited() else None

    def as_completeHandlerS(self):
        """
        A method that returns the result of as_completeHandler() method call on the flashObject.
        This method is used for handling the completion of the tooltip animation.

        :return: None
        """
        return self.flashObject.as_completeHandler() if self._isDAAPIInited() else None

   
