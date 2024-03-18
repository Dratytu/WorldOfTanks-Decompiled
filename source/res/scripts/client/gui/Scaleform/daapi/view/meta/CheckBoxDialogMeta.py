# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CheckBoxDialogMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent # Importing BaseDAAPIComponent to inherit from it

class CheckBoxDialogMeta(BaseDAAPIComponent):
    # Defining a method that gets called when the checkbox state changes
    def onCheckBoxChange(self, isSelected):
        # Print an error message if this method is overridden
        self._printOverrideError('onCheckBoxChange')

    # Defining an action script method that sets the label of the checkbox
    def as_setCheckBoxLabelS(self, value):
        # Return the result of as_setCheckBoxLabel if DAAPI is initialized
        return self.flashObject.as_setCheckBoxLabel(value) if self._isDAAPIInited() else None

    # Defining an action script method that sets the selected state of the checkbox
    def as_setCheckBoxSelectedS(self, value):
        # Return the result of as_setCheckBoxSelected if DAAPI is initialized
        return self.flashObject.as_setCheckBoxSelected(value) if self._isDAAPIInited() else None

    # Defining an action script method that sets the enabled state of the checkbox
    def as_setCheckBoxEnabledS(self, value):
        # Return the result of as_setCheckBoxEnabled if DAAPI is initialized
        return self.flashObject.as_setCheckBoxEnabled(value) if self._isDAAPIInited() else None
