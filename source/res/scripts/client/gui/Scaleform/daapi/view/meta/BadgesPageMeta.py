# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BadgesPageMeta.py

import weakref
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class BadgesPageMeta(WrapperViewMeta):
    # Defines a method to be called when the back button is clicked
    def onBackClick(self):
        self._printOverrideError('onBackClick')

    # Defines a method to be called when a badge is selected
    def onSelectBadge(self, badgeID):
        self._printOverrideError('onSelectBadge')

    # Defines a method to be called when a badge is deselected
    def onDeselectBadge(self):
        self._printOverrideError('onDeselectBadge')

    # Defines a method to be called when a suffix badge is selected
    def onSelectSuffixBadge(self, badgeID):
        self._printOverrideError('onSelectSuffixBadge')

    # Defines a method to be called when a suffix badge is deselected
    def onDeselectSuffixBadge(self):
        self._printOverrideError('onDeselectSuffixBadge')

    # Defines a method to be called when a dummy button is pressed
    def onDummyButtonPress(self):
        self._printOverrideError('onDummyButtonPress')

    # Sends the static data to the view
    def as_setStaticDataS(self, data):
        return self.flashObject.as_setStaticData(data) if self._isDAAPIInited() else None

    # Sends the received badges data to the view
    def as_setReceivedBadgesS(self, data):
        return self.flashObject.as_setReceivedBadges(data) if self._isDAAPIInited() else None

    # Sends the not received badges data to the view
    def as_setNotReceivedBadgesS(self, data):
        return self.flashObject.as_setNotReceivedBadges(data) if self._isDAAPIInited() else None

    # Sends the selected badge data and the selected state to the view
    def as_setSelectedBadgeS(self, data, selected):
        return self.flashObject.as_setSelectedBadge(data, selected) if self._
