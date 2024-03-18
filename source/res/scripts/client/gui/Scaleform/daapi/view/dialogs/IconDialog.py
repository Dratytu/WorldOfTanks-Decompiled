# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconDialog.py

# Import the necessary classes and functions.
from gui.Scaleform.daapi.view.meta.IconDialogMeta import IconDialogMeta

# Define the IconDialog class that inherits from IconDialogMeta.
class IconDialog(IconDialogMeta):

    # Initialize the IconDialog class with the given meta and handler.
    def __init__(self, meta, handler):
        # Call the constructor of the superclass with the message, title, button labels, and callback wrapper for the handler.
        super(IconDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))

        # Initialize the meta attribute with the given meta object.
        self._meta = meta

    # Override the _populate method of the superclass.
    def _populate(self):
        # Call the _populate method of the superclass.
        super(IconDialog, self)._populate()

        # Set the icon of the dialog to the icon specified in the meta object.
        self.as_setIconS(self._meta.getIcon())

    # Override the _dispose method of the superclass.
    def _dispose(self):
        # Set the meta attribute to None.
        self._meta = None

        # Call the _dispose method of the superclass.
        super(IconDialog, self)._dispose()

        # Return None.
        return

