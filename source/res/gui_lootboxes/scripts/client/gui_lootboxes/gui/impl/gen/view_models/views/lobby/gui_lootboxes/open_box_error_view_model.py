# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/open_box_error_view_model.py

# This script defines a ViewModel class named OpenBoxErrorViewModel, which is a part of the
# MVC (Model-View-Controller) architecture. ViewModels are used to manage the data and
# expose it to the View (GUI) for display and user interaction.

from frameworks.wulf import ViewModel  # Importing ViewModel from the wulf framework.

class OpenBoxErrorViewModel(ViewModel):
    # Inheriting from the ViewModel class and defining custom attributes and methods.

    __slots__ = ('toHangar',)  # Defining a fixed set of attributes to save memory.

    def __init__(self, properties=0, commands=1):
        # Initializing the OpenBoxErrorViewModel class with optional properties and commands.
        super(OpenBoxErrorViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        # Initializing the ViewModel attributes and methods.
        super(OpenBoxErrorViewModel, self)._initialize()
        self.toHangar = self._addCommand('toHangar')  # Adding a command to navigate to the hangar.
