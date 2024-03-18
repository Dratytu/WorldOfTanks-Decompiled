# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/hangar/fun_random_widget.py

# Import the necessary classes and functions for this module.
from fun_random.gui.impl.lobby.feature.fun_random_hangar_widget_view import FunRandomHangarWidgetView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor


class FunRandomHangarWidgetComponent(InjectComponentAdaptor):
    # Inherit from InjectComponentAdaptor class to enable automatic injection of components.

    def _makeInjectView(self):
        # Create an instance of the FunRandomHangarWidgetView class and return it.
        return FunRandomHangarWidgetView()

