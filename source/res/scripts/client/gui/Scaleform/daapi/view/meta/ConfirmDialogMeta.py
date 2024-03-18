# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmDialogMeta.py

import weakref
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmDialogMeta(AbstractWindowView):
    """
    Meta class for ConfirmDialog view.
    Inherits from AbstractWindowView, providing basic window functionality.
    """

    def __init__(self):
        """
        Initialize the ConfirmDialogMeta class.
        """
        super(ConfirmDialogMeta, self).__init__()
        self._weakRefs = {}

