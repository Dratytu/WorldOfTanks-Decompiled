# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoWindow.py

from gui.Scaleform.daapi.view.meta.FreeXPInfoWindowMeta import FreeXPInfoWindowMeta
__author__ = 'd_savitski'

class FreeXPInfoWindow(FreeXPInfoWindowMeta):
    """
    A dialog window for displaying information about free experience points.

    This class is a view component for the Free XP info window, which is displayed when the player
    clicks on the "Free XP" button in the garage. The window shows the current amount of free XP
    and allows the player to convert it to another type of experience points.

    Attributes:
        meta (dict): A dictionary containing metadata for the window, such as the title, submit
            button label, and text information.
        handler (callable): A callback function to be called when the window is closed.
    """

    def __init__(self, ctx=None):
        """
        Initializes the FreeXPInfoWindow instance.

        Args:
            ctx (dict, optional): A dictionary containing initialization data for the window.
        """
        super(FreeXPInfoWindow, self).__init__()
        self.meta = ctx.get('meta')
        self.handler = ctx.get('handler')

    def _populate(self):
        """
        Populates the window with data from the metadata dictionary.
        """
        super(FreeXPInfoWindow, self)._populate()
        self.as_setTitleS(self.meta.getTitle())
        self.as_setSubmitLabelS(self.meta.getSubmitLbl())
        self.as_setTextS(self.meta.getTextInfo())

    def onWindowClose(self):
        """
        Called when the window is closed.

        This method
