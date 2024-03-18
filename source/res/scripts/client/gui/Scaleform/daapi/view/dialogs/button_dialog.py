# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/button_dialog.py

# Import the SimpleDialog class from the dialogs module
from SimpleDialog import SimpleDialog

# Define the ButtonDialog class, which inherits from SimpleDialog
class ButtonDialog(SimpleDialog):

    # Define the _callHandler method, which is called when a button in the dialog is clicked
    def _callHandler(self, buttonID):
        # Check if the handler (a function or method to process button clicks) is set
        if self._handler is not None:
            # Call the handler, passing the ID of the clicked button
            self._handler(buttonID)
            
            # Set the _isProcessed attribute to True, indicating that the event has been handled
            self._isProcessed = True
        # If the handler is not set, do nothing
        return
