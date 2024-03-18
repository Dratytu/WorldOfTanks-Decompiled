# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseStorageCategoryViewMeta.py

from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent  # Importing BaseDAAPIComponent to inherit its properties and methods

class BaseStorageCategoryViewMeta(BaseDAAPIComponent):
    """
    Meta class for BaseStorageCategoryView, which is a view for displaying and managing storage categories.
    """

    def setActiveState(self, isActive):
        """
        Sets the active state of the view.

        :param isActive: A boolean value indicating whether the view is active or not.
        """
        self._printOverrideError('setActiveState')  # Prints an error message if this method is overridden

    def playInfoSound(self):
        """
        Plays an info sound.
        """
        self._printOverrideError('playInfoSound')  # Prints an error message if this method is overridden

    def scrolledToBottom(self):
        """
        Checks if the view is scrolled to the bottom.
        """
        self._printOverrideError('scrolledToBottom')  # Prints an error message if this method is overridden

    def as_showDummyScreenS(self, show):
        """
        Shows or hides a dummy screen.

        :param show: A boolean value indicating whether to show (True) or hide (False) the dummy screen.
        :return: None
        """
        return self.flashObject.as_showDummyScreen(show) if self._isDAAPIInited() else None  # Returns the result of the corresponding AS method if DAAPI is initialized

    def as_showFilterWarningS(self, data):
        """
        Shows a filter warning.

        :param data: The data to be displayed in the warning.
        :return: None
        """
        return self.flashObject.as_showFilterWarning(data) if self._isDAAPIInited()
