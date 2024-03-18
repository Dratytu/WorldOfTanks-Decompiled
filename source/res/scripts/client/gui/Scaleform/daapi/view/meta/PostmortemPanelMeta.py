# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PostmortemPanelMeta.py

# This file defines the PostmortemPanelMeta class, which is a subclass of BasePostmortemPanelMeta.
# It provides a user interface for displaying information about a player's death in a game.

from gui.Scaleform.daapi.view.meta.BasePostmortemPanelMeta import BasePostmortemPanelMeta  # Importing BasePostmortemPanelMeta class.

class PostmortemPanelMeta(BasePostmortemPanelMeta):

    # onDogTagKillerInPlaySound method is called when the dog tag of the killer is played in the game.
    def onDogTagKillerInPlaySound(self):
        self._printOverrideError('onDogTagKillerInPlaySound')  # Prints an error message if this method is overridden.

    # onDogTagKillerOutPlaySound method is called when the dog tag of the killer is no longer played in the game.
    def onDogTagKillerOutPlaySound(self):
        self._printOverrideError('onDogTagKillerOutPlaySound')  # Prints an error message if this method is overridden.

    # onVictimDogTagInPlaySound method is called when the dog tag of the victim is played in the game.
    def onVictimDogTagInPlaySound(self):
        self._printOverrideError('onVictimDogTagInPlaySound')  # Prints an error message if this method is overridden.

    # as_showDeadReasonS method is used to display the reason for the player's death.
    def as_showDeadReasonS(self):
        return self.flashObject.as_showDeadReason() if self._isDAAPIInited() else None  # Returns the result of the as_showDeadReason method if DAAPI is initialized, otherwise returns None.

    # as_setPlayerInfoS method is used to set the player information.
    def as_setPlayerInfoS(self, playerInfo):
        self.flashObject.as_setPlayerInfo(playerInfo) if self._isDAAPIInited() else None  # Calls the
