# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/dialogs/sub_views/top_right/br_money_balance.py

# Import necessary modules and classes
from battle_royale.gui.impl.dialogs import CurrencyTypeExtended
from gui.impl.dialogs.dialog_template_tooltip import DialogTemplateTooltip
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_royale.dialogs.sub_views.br_money_balance_view_model import BrMoneyBalanceViewModel
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleRentVehiclesController

# Define the BRMoneyBalance class, inheriting from MoneyBalance
class BRMoneyBalance(MoneyBalance):
    # Inject IBattleRoyaleRentVehiclesController dependency
    __rentVehiclesController = dependency.descriptor(IBattleRoyaleRentVehiclesController)

    # Class constructor
    def __init__(self):
        # Call the parent class constructor
        super(BRMoneyBalance, self).__init__(R.views.dialogs.sub_views.topRight.BRMoneyBalance(), BrMoneyBalanceViewModel())

    # Property for accessing the view model
    @property
    def viewModel(self):
        return self.getViewModel()

    # Override createToolTipContent method to handle custom tooltip content
    def createToolTipContent(self, event, contentID):
        if contentID == R.views.dialogs.common.DialogTemplateGenericTooltip():
            currency = event.getArgument('currency')
            factory = self._tooltips.get(CurrencyTypeExtended(currency))
            if factory and factory.tooltipFactory is not None:
                return factory.tooltipFactory()
        return super(BRMoneyBalance, self).createToolTipContent(event, contentID)

    # Override _onLoading method to set up event handlers
    def _onLoading(self, *args, **kwargs):
        super(BRMoneyBalance, self)._onLoading(*args, **kwargs)
        self.__rentVehiclesController.onBalanceUpdated += self.__onBalanceUpdated

    # Override _finalize method to clean up event handlers
    def _finalize(self):
        self.__rentVehiclesController.onBalanceUpdated -= self.__onBalanceUpdated
        super(BRMoneyBalance, self)._finalize()

    # Initialize tooltips
    def _initTooltips(self):
        model = self.viewModel
        return {CurrencyTypeExtended.CREDITS: DialogTemplateTooltip(viewModel=model.creditsTooltip),
                CurrencyTypeExtended.BR_COIN: DialogTemplateTooltip(viewModel=model.brcoinsTooltip)}

    # Update the view model with relevant data
    def _updateModel(self, model):
        isWGMAvailable = self._stats.mayConsumeWalletResources
        model.setIsWGMAvailable(isWGMAvailable)
        model.setCredits(int(self._stats.money.getSignValue(Currency.CREDITS)))
        brCoin = self.__rentVehiclesController.getBRCoinBalance(0)
        model.setBrcoins(brCoin)

    # Handle balance update event
    def __onBalanceUpdated(self):
        self._moneyChangeHandler()
