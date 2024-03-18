# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AcousticPopoverMeta.py

# This script defines a meta class 'AcousticPopoverMeta' which inherits from 'SmartPopOverView'.
# The class is used for creating Acoustic Popover views in the game UI.

from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView  # Importing the SmartPopOverView class.

class AcousticPopoverMeta(SmartPopOverView):

    # onActionStart method is called when an action is started in the Acoustic Popover view.
    def onActionStart(self, actionID):
        # This line raises an exception since the method is not implemented in this meta class.
        # It should be implemented in the corresponding ActionScript class.
        self._printOverrideError('onActionStart')

    # onSpeakerClick method is called when a speaker is clicked in the Acoustic Popover view.
    def onSpeakerClick(self, speakerID):
        # This line raises an exception since the method is not implemented in this meta class.
        # It should be implemented in the corresponding ActionScript class.
        self._printOverrideError('onSpeakerClick')

    # as_setDataS method is used to set data for the Acoustic Popover view.
    def as_setDataS(self, data):
        # This method returns the result of the 'as_setData' method called on the flashObject.
        # The '_isDAAPIInited()' method is used to check if the DAAPI is initialized.
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    # as_onItemPlayS method is called when an item is played in the Acoustic Popover view.
    def as_onItemPlayS(self, itemsID):
        # This method returns the result of the 'as_onItemPlay' method called on the flashObject.
        return self.flash
