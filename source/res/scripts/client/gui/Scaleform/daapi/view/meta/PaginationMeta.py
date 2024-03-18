# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PaginationMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent as BaseDAAPIComponent # Importing BaseDAAPIComponent from the Scaleform framework.

class PaginationMeta(BaseDAAPIComponent):

    # showPage method is overridden, but the override is not implemented.
    # It is recommended to either implement the method or remove the override.
    def showPage(self, dir):
        self._printOverrideError('showPage')

    # as_setPageS method is used to set the current page value in the UI.
    def as_setPageS(self, value):
        # If the DAAPI is initialized, return the result of as_setPage method called on the flashObject.
        return self.flashObject.as_setPage(value) if self._isDAAPIInited() else None

    # as_setEnabledS method is used to set the enabled/disabled state of left and right buttons in the UI.
    def as_setEnabledS(self, leftEnabled, rightEnabled):
        # If the DAAPI is initialized, return the result of as_setEnabled method called on the flashObject.
        return self.flashObject.as_setEnabled(leftEnabled, rightEnabled) if self._isDAAPIInited() else None

