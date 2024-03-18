# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractPopOverView.py

# Import necessary classes and functions
from gui.Scaleform.daapi.view.meta.PopOverViewMeta import PopOverViewMeta
from gui.shared.events import HidePopoverEvent

# Define the AbstractPopOverView class, which is a subclass of PopOverViewMeta
class AbstractPopOverView(PopOverViewMeta):

    # Constructor for the AbstractPopOverView class
    def __init__(self, ctx=None):
        # Call the constructor of the superclass
        super(AbstractPopOverView, self).__init__()

    # This method is called when the view is populated with data
    def _populate(self):
        # Call the _populate method of the superclass
        super(AbstractPopOverView, self)._populate()

        # Add a listener for the HidePopoverEvent event with the handler _handlerHidePopover
        self.addListener(HidePopoverEvent.HIDE_POPOVER, self._handlerHidePopover)

    # Handler for the HidePopoverEvent event
    def _handlerHidePopover(self, event):
        # Destroy the view
        self.destroy()

    # This method is called when the view is being disposed
    def _dispose(self):
        # Remove the listener for the HidePopoverEvent event
        self.removeListener(HidePopoverEvent.HIDE_POPOVER, self._handlerHidePopover)

        # Call the _dispose method of the superclass
        super(AbstractPopOverView, self)._dispose()

        # Fire the HidePopoverEvent event with the POPOVER_DESTROYED argument
        self.fireEvent(HidePopover
