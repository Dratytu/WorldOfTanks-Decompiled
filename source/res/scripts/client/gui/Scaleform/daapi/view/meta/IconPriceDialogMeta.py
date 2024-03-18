# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconPriceDialogMeta.py

# Import the IconDialog class from the gui.Scaleform.daapi.view.dialogs module
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog

# Define the IconPriceDialogMeta class, which inherits from the IconDialog class
class IconPriceDialogMeta(IconDialog):

    # Define the as_setMessagePriceS method, which takes dialogData as a parameter
    def as_setMessagePriceS(self, dialogData):
        # If the DAAPI is initialized, call the as_setMessagePrice method on the flashObject with dialogData as an argument
        return self.flashObject.as_setMessagePrice(dialogData) if self._isDAAPIInited() else None

    # Define the as_setPriceLabelS method, which takes label as a parameter
    def as_setPriceLabelS(self, label):
        # If the DAAPI is initialized, call the as_setPriceLabel method on the flashObject with label as an argument
        return self.flashObject.as_setPriceLabel(label) if self._isDAAPIInited() else None

    # Define the as_setOperationAllowedS method, which takes isAllowed as a parameter
    def as_setOperationAllowedS(self, isAllowed):
        # If the DAAPI is initialized, call the as_setOperationAllowed method on the flashObject with isAllowed as an argument
        return self.flashObject.as_setOperationAllowed(isAllowed) if self._isDAAPIInited() else None

