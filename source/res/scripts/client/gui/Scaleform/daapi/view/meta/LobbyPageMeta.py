# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyPageMeta.py

import abc

class LobbyPageMeta(View):
    """ The meta-class for lobby pages in the game UI.
    Inherits from `View`. """

    def moveSpace(self, x, y, delta):
        """ Override error message printer for the `moveSpace` method. """
        self._printOverrideError('moveSpace')

    def getSubContainerTypes(self):
        """ Override error message printer for the `getSubContainerTypes` method. """
        self._printOverrideError('getSubContainerTypes')

    def notifyCursorOver3dScene(self, isOver3dScene):
        """ Override error message printer for the `notifyCursorOver3dScene` method. """
        self._printOverrideError('notifyCursorOver3dScene')

    def notifyCursorDragging(self, isDragging):
        """ Override error message printer for the `notifyCursorDragging` method. """
        self._printOverrideError('notifyCursorDragging')

    def as_showHelpLayoutS(self):
        """ Dispatches the `showHelpLayout` signal to the client. """
        return self.flashObject.as_showHelpLayout() if self._isDAAPIInited() else None

    def as_closeHelpLayoutS(self):
        """ Dispatches the `closeHelpLayout` signal to the client. """
        return self.flashObject.as_closeHelpLayout() if self._isDAAPIInited() else None

    def as_showWaitingS(self, message):
        """ Dispatches the `showWaiting` signal with the given message to the client. """
        return self.flashObject.as_showWaiting(message) if self._isDAAPIInited() else None

    def as_hideWaitingS(self):
        """ Dispatches the `hideWaiting` signal to the client. """
        return self.flashObject.as_hideWaiting() if self._
