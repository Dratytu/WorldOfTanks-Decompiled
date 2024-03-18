# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleMattersViewMeta.py

import sys
from gui.Scaleform.daapi.view.meta.MissionsViewBaseMeta import MissionsViewBaseMeta # Importing MissionsViewBaseMeta class

class BattleMattersViewMeta(MissionsViewBaseMeta):

    # as_showViewS() method is used to show the view
    def as_showViewS(self):
        return self.flashObject.as_showView() if self._isDAAPIInited() else None # If DAAPI is initialized, call as_showView() on the flashObject, otherwise return None

    # as_hideViewS() method is used to hide the view
    def as_hideViewS(self):
        return self.flashObject.as_hideView() if self._isDAAPIInited() else None # If DAAPI is initialized, call as_hideView() on the flashObject, otherwise return None

    # as_setPlaceIdS() method is used to set the place ID
    def as_setPlaceIdS(self, placeId):
        return self.flashObject.as_setPlaceId(placeId) if self._isDAAPIInited() else None # If DAAPI is initialized, call as_setPlaceId() on the flashObject with the provided placeId, otherwise return None

