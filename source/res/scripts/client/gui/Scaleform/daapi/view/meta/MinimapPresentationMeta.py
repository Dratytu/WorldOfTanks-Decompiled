# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapPresentationMeta.py

import sys
if sys.version_info[0] < 3:
    input = raw_input  # noqa F821

from gui.Scaleform.daapi.view.meta.MinimapEntityMeta import MinimapEntityMeta

# Subclass of MinimapEntityMeta specifically for minimap presentations
class MinimapPresentationMeta(MinimapEntityMeta):

    # Sets the map (arena) for the minimap presentation
    def setMap(self, arenaID):
        self._printOverrideError('setMap')

    # Sets the minimap data, including the arena ID, player team, and size
    def setMinimapData(self, arenaID, playerTeam, size):
        self._printOverrideError('setMinimapData')

    # Changes the map texture on the minimap presentation
    def as_changeMapS(self, texture):
        return self.flashObject.as_changeMap(texture) if self._isDAAPIInited() else None

    # Adds a point to the minimap presentation with the given coordinates, type, color, and id
    def as_addPointS(self, x, y, type, color, id):
        return self.flashObject.as_addPoint(x, y, type, color, id) if self._isDAAPIInited() else None

    # Adds a point of interest (POI) to the minimap presentation with the given coordinates and type
    def as_addPoiS(self, x, y, type, id):
        return self.flashObject.as_addPoi(x, y, type, id) if self._isDAAPIInited() else None

    # Clears all points and POIs from the minimap presentation
    def as_clearS(self):
        return self.flashObject.as_clear() if self._isDAAPI
