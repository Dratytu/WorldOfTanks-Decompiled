# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattlesListWindow.py

# Import necessary classes and interfaces
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView
from gui.prb_control.entities.listener import IGlobalListener
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

# Define the PrebattlesListWindow class, which inherits from AbstractWindowView and IGlobalListener
class PrebattlesListWindow(AbstractWindowView, IGlobalListener):

    # Class constructor, initializes the PrebattlesListWindow instance
    def __init__(self, name):
        super(PrebattlesListWindow, self).__init__()
        self._name = name
        self.isMinimising = False

    # Property to access the chat component
    @property
    def chat(self):
        chat = None
        if MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT in self.components:
            chat = self.components[MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT]
        return chat


