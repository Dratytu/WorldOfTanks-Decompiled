# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PerksPanelMeta.py

import sys
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent # Importing BaseDAAPIComponent from the gui.Scaleform.framework.entities module

class PerksPanelMeta(BaseDAAPIComponent):

    def as_setPerksS(self, items):
        # as_setPerks(items) method is called on the flashObject if it has been initialized
        return self.flashObject.as_setPerks(items) if self._isDAAPIInited() else None

    def as_updatePerkS(self, perkName, state, duration, lifeTime):
        # as_updatePerk(perkName, state, duration, lifeTime) method is called on the flashObject if it has been initialized
        return self.flashObject.as_updatePerk(perkName, state, duration, lifeTime) if self._isDAAPIInited() else None

    def as_clearPanelS(self):
        # as_clearPanel() method is called on the flashObject if it has been initialized
        return self.flashObject.as_clearPanel() if self._isDAAPIInited() else None

