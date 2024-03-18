# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/players_panel.py

# Import necessary constants and helper classes
from constants import ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.comp7.comp7_voip_helper import Comp7VoipHelper, VoiceChatControlTextStyles
from gui.Scaleform.daapi.view.meta.Comp7PlayersPanelMeta import Comp7PlayersPanelMeta

# Define the PlayersPanel class, which inherits from Comp7PlayersPanelMeta
class PlayersPanel(Comp7PlayersPanelMeta):
    
    # Initialize the class with default settings
    def __init__(self):
        super(PlayersPanel, self).__init__()
        self.__voipHelper = Comp7VoipHelper(component=self, textStyle=VoiceChatControlTextStyles.PLAYERS_PANEL)

    # Handle the click event for the voice chat control
    def onVoiceChatControlClick(self):
        self.__voipHelper.onVoiceChatControlClick()

    # Set the period and enable/disable the voip control accordingly
    def setPeriod(self, period):
        self.__voipHelper.enable(enable=self.__isVoipControlEnabled(period))

    # Populate the panel with necessary data
    def _populate(self):
        super(PlayersPanel, self)._populate()
        self.__voipHelper.populate()
        self.__voipHelper.enable(enable=self.__isVoipControlEnabled())

    # Dispose of the panel and its resources
    def _dispose(self):
        self.__voipHelper.dispose()
        super(PlayersPanel, self)._dispose()

    # Static method to check if the voip control should be enabled
    @classmethod
    def __isVoipControlEnabled(cls, period=None):
        if period is None:
            period = cls.sessionProvider.shared.arenaPeriod.getPeriod()
        return period == ARENA_PERI
