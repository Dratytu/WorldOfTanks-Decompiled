# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapPromoView.py

# Import necessary helpers and libraries
from helpers.i18n import makeString as _ms # Helper function for localization
from gui.Scaleform.locale.CLANS import CLANS # Localization constants for clan-related text
from gui.Scaleform.locale.RES_ICONS import RES_ICONS # Localization constants for icons
from gui.shared.formatters import text_styles # Helper functions for formatting text
from gui.shared.events import OpenLinkEvent # Event for opening links
from gui.Scaleform.daapi.view.meta.ClanProfileGlobalMapPromoViewMeta import ClanProfileGlobalMapPromoViewMeta # Base class for the view

class ClanProfileGlobalMapPromoView(ClanProfileGlobalMapPromoViewMeta):

    # Method to show info link
    def showInfo(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_PROMO))

    # Method to show map link
    def showMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_CAP))

    # Override the _populate method to set view data
    def _populate(self):
        super(ClanProfileGlobalMapPromoView, self)._populate()

        # Set data for the view
        self.as_setDataS({
            # Header text
            'header': text_styles.promoSubTitle(_ms(CLANS.GLOBALMAPVIEW_PROMO_HEADER)),
            # Description text
            'description': text_styles.main(_ms(CLANS.GLOBALMAPVIEW_PROMO_DESCRIPTION)),
            # Info link label
            'infoLinkLabel': _ms(CLANS.GLOBALMAPVIEW_PROMO_INFOLINK),
            # Map link label
            'mapLinkLabel': _ms
