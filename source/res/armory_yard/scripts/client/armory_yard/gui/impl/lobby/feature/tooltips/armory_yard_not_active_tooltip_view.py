# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/lobby/feature/tooltips/armory_yard_not_active_tooltip_view.py

# Import necessary modules and classes
import armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.entry_point_not_active_tooltip_view_model as model
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

# Define the EntryPointNotActiveTooltipView class, which inherits from ViewImpl
class EntryPointNotActiveTooltipView(ViewImpl):
    # Declare an empty __slots__ attribute to save memory by preventing the creation of a dictionary for each instance
    __slots__ = ()

    # Define the constructor method for the EntryPointNotActiveTooltipView class
    def __init__(self):
        # Initialize settings for the view using ViewSettings, specifying the view's embedded file name and model
        settings = ViewSettings(R.views.armory_yard.lobby.feature.tooltips.EntryPointNotActiveTooltipView())
        settings.model = model.EntryPointNotActiveTooltipViewModel()  # Set the view's model
        super(EntryPointNotActiveTooltipView, self).__init__(settings)  # Initialize the parent class (ViewImpl) with the settings

    # Define a method to get the view model
    def viewModel(self):
        return super(EntryPointNotActiveTooltipView, self).getViewModel()  # Return the view's model
