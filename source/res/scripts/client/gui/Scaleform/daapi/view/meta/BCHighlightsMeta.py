# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCHighlightsMeta.py

import flashObject  # For accessing Scaleform methods (e.g., as_setDescriptors, as_addHighlight, as_removeHighlight)
from gui.Scaleform.framework.entities.View import View  # Base class for all Scaleform views

class BCHighlightsMeta(View):

    # Called when a component is triggered (e.g., clicked)
    def onComponentTriggered(self, highlightId):
        self._printOverrideError('onComponentTriggered')

    # Called when a highlight animation is completed
    def onHighlightAnimationComplete(self, highlightId):
        self._printOverrideError('onHighlightAnimationComplete')

    # Set descriptors for the view
    def as_setDescriptorsS(self, data):
        return self.flashObject.as_setDescriptors(data) if self._isDAAPIInited() else None

    # Add a highlight with the given ID
    def as_addHighlightS(self, highlightId):
        return self.flashObject.as_addHighlight(highlightId) if self._isDAAPIInited() else None

    # Remove a highlight with the given ID
    def as_removeHighlightS(self, highlightId):
        return self.flashObject.as_removeHighlight(highlightId) if self._isDAAPIInited() else None

