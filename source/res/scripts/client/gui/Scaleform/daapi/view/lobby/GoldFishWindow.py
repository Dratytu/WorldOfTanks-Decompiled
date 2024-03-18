# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/GoldFishWindow.py

# Import necessary modules and classes
from account_helpers.AccountSettings import AccountSettings, GOLD_FISH_LAST_SHOW_TIME
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES
from gui.Scaleform.daapi.view.meta.GoldFishWindowMeta import GoldFishWindowMeta
from gui.Scaleform.genConsts.TEXT_ALIGN import TEXT_ALIGN
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.gold_fish import isGoldFishActionActive
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared import events
from helpers.time_utils import getCurrentTimestamp

# Define constants
BTN_WIDTH = 120

class GoldFishWindow(GoldFishWindowMeta):

    def __init__(self, _=None):
        # Initialize the superclass
        super(GoldFishWindow, self).__init__()

    def onBtnClick(self, action):
        # Event handler for button clicks
        if action == 'closeAction':
            self.onWindowClose()

    def eventHyperLinkClicked(self):
        # Event handler for hyperlink clicks
        self.fireEvent(events.OpenLinkEvent(events.OpenLinkEvent.PAYMENT))

    def onWindowClose(self):
        # Event handler for window close events
        if isGoldFishActionActive():
            AccountSettings.setFilter(GOLD_FISH_LAST_SHOW_TIME, getCurrentTimestamp())
            self.fireEvent(events.CloseWindowEvent(events.CloseWindowEvent.GOLD_FISH_CLOSED), EVENT_BUS_SCOPE.LOBBY)
        self.destroy()

    def _populate(self):
        # Override the superclass's _populate method
        super(GoldFishWindow, self)._populate()

        # Set the image source, window title, and texts
        self.as_setImageS(RES_ICONS.MAPS_ICONS_WINDOWS_GOLDFISH_GOLDFISHBG, 0)
        self.as_setWindowTitleS(MENU.GOLDFISH_WINDOWHEADER)
        self.as_setWindowTextsS(MENU.GOLDFISH_HEADER, MENU.GOLDFISH_EVENTTITLE, MENU.GOLDFISH_EVENTTEXT, MENU.GOLDFISH_EVENTLINK)

        # Set the button properties
        self.as_setButtonsS([{'label': MENU.GOLDFISH_BUTTONCLOSE,
          'btnLinkage': BUTTON_LINKAGES.BUTTON_BLACK,
          'action': 'closeAction',
          'isFocused': True,
          'tooltip': ''}], TEXT_ALIGN.RIGHT, BTN_WIDTH)

