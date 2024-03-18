# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/reward_currency_tooltip_view.py

# Import necessary modules and classes
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.reward_currency_tooltip_view_model import RewardCurrencyTooltipViewModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

# Define the RewardCurrencyTooltipView class, which inherits from ViewImpl
class RewardCurrencyTooltipView(ViewImpl):
    
    # Initialize the class with a currencyType parameter
    def __init__(self, currencyType):
        # Set up view settings with the specified currency type
        settings = ViewSettings(R.views.battle_royale.lobby.tooltips.RewardCurrencyTooltipView())
        settings.model = RewardCurrencyTooltipViewModel()
        self.__currencyType = currencyType
        super(RewardCurrencyTooltipView, self).__init__(settings)

    # Property to access the view model
    @property
    def viewModel(self):
        return super(RewardCurrencyTooltipView, self).getViewModel()

    # Event handler for the loading of the view
    def _onLoading(self, *args, **kwargs):
        # Call the parent class's _onLoading method
        super(RewardCurrencyTooltipView, self)._onLoading(args, kwargs)
        # Set the currency type in the view model
        self.viewModel.setCurrencyType(self.__currencyType)

