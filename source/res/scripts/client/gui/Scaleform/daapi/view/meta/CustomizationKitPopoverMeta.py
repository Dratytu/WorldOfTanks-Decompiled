# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationKitPopoverMeta.py

import flashcall
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView # Importing SmartPopOverView class from the lobby.popover package

class CustomizationKitPopoverMeta(SmartPopOverView):

    # Defining a method to remove the customization kit
    def removeCustomizationKit(self):
        self._printOverrideError('removeCustomizationKit')

    # Defining a method to update the auto-prolongation setting
    def updateAutoProlongation(self):
        self._printOverrideError('updateAutoProlongation')

    # as_setHeaderS: A flashcall method to set the popover header text
    @flashcall
    def as_setHeaderS(self, title):
        return self.flashObject.as_setHeader(title) if self._isDAAPIInited() else None

    # as_getDPS: A flashcall method to get the Daily Progress Summary
    @flashcall
    def as_getDPS(self):
        return self.flashObject.as_getDP() if self._isDAAPIInited() else None

    # as_showClearMessageS: A flashcall method to show a confirmation message when clearing the customization kit
    @flashcall
    def as_showClearMessageS(self, isClear, message):
        return self.flashObject.as_showClearMessage(isClear, message) if self._isDAAPIInited() else None

    # as_setAutoProlongationCheckboxSelectedS: A flashcall method to set the state of the auto-prolongation checkbox
    @flashcall
    def as_setAutoProlongationCheckboxSelectedS(self, value):
        return self.flashObject.as_setAutoProlongationCheckboxSelected(value) if self._isDAAPIInited() else None

    # as_setAuto
