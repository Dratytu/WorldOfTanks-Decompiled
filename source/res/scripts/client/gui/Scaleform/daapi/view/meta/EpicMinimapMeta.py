# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicMinimapMeta.py

# Import the MinimapComponent class from the gui.Scaleform.daapi.view.battle.shared.minimap.component module
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent

# Define the EpicMinimapMeta class, which inherits from the MinimapComponent class
class EpicMinimapMeta(MinimapComponent):

    # Define the onZoomModeChanged method, which takes a single argument 'change'
    def onZoomModeChanged(self, change):
        # Print an error message indicating that the method has been overridden
        self._printOverrideError('onZoomModeChanged')

    # Define the as_setZoomModeS method, which takes two arguments 'mode' and 'modeText'
    def as_setZoomModeS(self, mode, modeText):
        # If the DAAPI has been initialized, call the as_setZoomMode method on the flashObject with 'mode' and 'modeText' as arguments
        return self.flashObject.as_setZoomMode(mode, modeText) if self._isDAAPIInited() else None

    # Define the as_setMapDimensionsS method, which takes two arguments 'widthPx' and 'heightPx'
    def as_setMapDimensionsS(self, widthPx, heightPx):
        # If the DAAPI has been initialized, call the as_setMapDimensions method on the flashObject with 'widthPx' and 'heightPx' as arguments
        return self.flashObject.as_setMapDimensions(widthPx, heightPx) if self._isDAAPIInited() else None

    # Define the as_updateSectorStateStatsS method, which takes a single argument 'data'
    def as_updateSectorStateStatsS(self, data):
        # If the DAAPI has been initialized, call the as
