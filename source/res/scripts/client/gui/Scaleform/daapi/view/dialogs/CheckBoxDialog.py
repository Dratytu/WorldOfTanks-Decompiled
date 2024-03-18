# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/CheckBoxDialog.py

# Import the ConfirmDialogMeta class from the gui.Scaleform.daapi.view.meta package.
# This class is the meta for the CheckBoxDialog, which is a dialog with a checkbox.
from gui.Scaleform.daapi.view.meta.ConfirmDialogMeta import ConfirmDialogMeta

# Define the CheckBoxDialog class, which inherits from ConfirmDialogMeta.
class CheckBoxDialog(ConfirmDialogMeta):

    # Initialize the class with the meta and handler arguments.
    def __init__(self, meta, handler):
        # Call the constructor of the superclass (ConfirmDialogMeta).
        super(CheckBoxDialog, self).__init__()
        # Store the meta and handler arguments as instance variables.
        self.meta = meta
        self.handler = handler

    # This method is called when the user interacts with the dialog.
    def _callHandler(self, success, selected):
        # If the handler instance variable is not None, call the handler with the success and selected arguments.
        if self.handler is not None:
            self.handler((success, selected))
        # Return None.
        return

    # This method is called when the dialog is displayed.
    def _populate(self):
        # Call the _populate method of the superclass (ConfirmDialogMeta).
        super(CheckBoxDialog, self)._populate()
        # Get the button labels from the meta instance variable.
        buttonLabels = self.meta.getButtonsSubmitCancel()
        # Call the as_setSettingsS method of the dialog with the settings dictionary as an argument.
        self.as_setSettingsS({'title': self.meta.getTitle(),
         'description': self.meta.getMessage(),
         'submitBtnLabel': buttonLabels['submit'],
         'cancelBtnLabel': buttonLabels['cancel'],
         'checkBoxLabel': self.meta.getCheckBoxButtonLabel(),
         'checkBoxSelected': self.meta.getCheckBoxSelected()})

    # This method is called when the dialog is closed.
    def _dispose(self):
        # Set
