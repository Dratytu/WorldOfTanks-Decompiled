# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_container_view_model.py

import frameworks.wulf as wulf
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_container_tab_model import FrontlineContainerTabModel

# Define a ViewModel class for the FrontlineContainerView
class FrontlineContainerViewModel(wulf.ViewModel):
    # Define the names of properties and commands
    __slots__ = ('on_tab_change', 'on_close')

    def __init__(self, properties=2, commands=2):
        # Initialize the ViewModel with the given properties and commands
        super(FrontlineContainerViewModel, self).__init__(properties=properties, commands=commands)

    def get_current_tab_id(self):
        # Get the current tab ID
        return self._get_number(0)

    def set_current_tab_id(self, value):
        # Set the current tab ID
        self._set_number(0, value)

    def get_tabs(self):
        # Get the list of tabs
        return self._get_array(1)

    def set_tabs(self, value):
        # Set the list of tabs
        self._set_array(1, value)

    # Static method to get the type of elements in the 'tabs' Array
    @staticmethod
    def get_tabs_type():
        return FrontlineContainerTabModel

    def _initialize(self):
        # Initialize the ViewModel
        super(FrontlineContainerViewModel, self)._initialize()

        # Add 'currentTabId' Number property with a default value of 0
        self._add_number_property('currentTabId', 0)

        # Add 'tabs' Array property
        self._add_array_property('tabs', wulf.Array())

        # Add '
