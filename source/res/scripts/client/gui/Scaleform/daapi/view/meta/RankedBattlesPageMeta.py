# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesPageMeta.py

# This is the base class for all Scaleform views in the application
from gui.Scaleform.framework.entities.View import View

# This class represents the RankedBattlesPage view in the Scaleform framework
class RankedBattlesPageMeta(View):

    # This method is called when the user clicks the close button on the view
    def onClose(self):
        # This line raises a NotImplementedError if the method is not overridden in a subclass
        self._printOverrideError('onClose')

    # This method is called when the user changes the page in the view
    def onPageChanged(self, viewId):
        # This line raises a NotImplementedError if the method is not overridden in a subclass
        self._printOverrideError('onPageChanged')

    # This method sends the 'setData' event to the view, passing the 'data' argument
    def as_setDataS(self, data):
        # This line returns the result of the 'as_setData' method on the flashObject, if the DAAPI is initialized
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    # This method sends the 'setHeaderData' event to the view, passing the 'data' argument
    def as_setHeaderDataS(self, data):
        # This line returns the result of the 'as_setHeaderData' method on the flashObject, if the DAAPI is initialized
        return self.flashObject.as_setHeaderData(data) if self._isDAAPIInited() else None

    # This method sends the 'setCounters' event to the view, passing the 'countersData' argument
    def as_setCountersS(self, countersData):
        # This line returns the result of the 'as_setCounters' method on the flashObject, if the DAAPI is initialized
