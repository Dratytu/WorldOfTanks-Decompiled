# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicDeploymentMapMeta.py

# Import the EpicMinimapMeta class from the EpicMinimapMeta module
from gui.Scaleform.daapi.view.meta.EpicMinimapMeta import EpicMinimapMeta

# Define the EpicDeploymentMapMeta class, which inherits from the EpicMinimapMeta class
class EpicDeploymentMapMeta(EpicMinimapMeta):

    # Define the as_setMapDimensionsS method, which takes two arguments: widthPx and heightPx
    def as_setMapDimensionsS(self, widthPx, heightPx):
        # Call the as_setMapDimensions method of the flashObject attribute, passing widthPx and heightPx as arguments
        # If the _isDAAPIInited method returns True
        return self.flashObject.as_setMapDimensions(widthPx, heightPx) if self._isDAAPIInited() else None

