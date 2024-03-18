# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/hangar/fun_random_widget.py

# Import the necessary classes and functions for this module.
from fun_random.gui.impl.lobby.feature.fun_random_hangar_widget_view import FunRandomHangarWidgetView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor  # Inherit from InjectComponentAdaptor class to enable automatic injection of components.


class FunRandomHangarWidgetComponent(InjectComponentAdaptor):
    # Create a custom component class for the fun_random feature in the hangar screen.

    def _makeInjectView(self):
        # Override the _makeInjectView method to return an instance of the custom FunRandomHangarWidgetView.
        # This method is called by the parent class when the component is initialized.
        return FunRandomHangarWidgetView()  # Create an instance of the FunRandomHangarWidgetView class and return it.

