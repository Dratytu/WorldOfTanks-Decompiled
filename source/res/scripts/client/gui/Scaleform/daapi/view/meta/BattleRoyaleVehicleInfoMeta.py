# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleVehicleInfoMeta.py

# Import View class from gui.Scaleform.framework.entities.View, which is the base class for this meta class
from gui.Scaleform.framework.entities.View import View

# Define the BattleRoyaleVehicleInfoMeta class, which inherits from View
class BattleRoyaleVehicleInfoMeta(View):

    # Define the onClose method, which is called when the window is closed
    def onClose(self):
        # Print an error message if the method is overridden but not implemented
        self._printOverrideError('onClose')

    # Define the as_setDataS method, which is used to set data on the client side
    def as_setDataS(self, data):
        # Call the as_setData method on the flashObject if the DAAPI is initialized, otherwise return None
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

