# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalReservesWidgetInjectMeta.py

# Import InjectComponentAdaptor class from gui.Scaleform.framework.entities.inject_component_adaptor
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

# Define the PersonalReservesWidgetInjectMeta class, which inherits from InjectComponentAdaptor
class PersonalReservesWidgetInjectMeta(InjectComponentAdaptor):

    # Define the as_setTargetWidthS method, which takes a single argument 'value'
    def as_setTargetWidthS(self, value):
        # If the DAAPI is initialized, call the as_setTargetWidth method on the flashObject with 'value' as an argument
        return self.flashObject.as_setTargetWidth(value) if self._isDAAPIInited() else None

