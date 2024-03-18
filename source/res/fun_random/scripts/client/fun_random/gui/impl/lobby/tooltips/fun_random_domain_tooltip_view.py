# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_domain_tooltip_view.py

# Importing necessary classes and functions
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView
from fun_random.gui.feature.util.fun_mixins import FunSubModeHolder
from fun_random.gui.feature.util.fun_wrappers import hasHoldingSubMode

# Defining the FunRandomDomainTooltipView class, which inherits from ModifiersDomainTooltipView and FunSubModeHolder
class FunRandomDomainTooltipView(ModifiersDomainTooltipView, FunSubModeHolder):

    # Decorated method to ensure a sub-mode is being held before continuing
    @hasHoldingSubMode()
    def getModifiersDataProvider(self):
        # Returns the modifiers data provider for the holding sub-mode
        return self.getHoldingSubMode().getModifiersDataProvider()

    # Overriding the _onLoading method from the parent class
    def _onLoading(self, subModeID=None, *args, **kwargs):
        # Catching the sub-mode with the given ID or the desired sub-mode ID from the _funRandomCtrl
        self.catchSubMode(subModeID or self._funRandomCtrl.subModesHolder.getDesiredSubModeID())
        # Calling the parent class's _onLoading method with the provided arguments
        super(FunRandomDomainTooltipView, self)._onLoading(*args, **kwargs)

    # Overriding the _finalize method from the parent class
    def _finalize(self):
        # Calling the parent class's _finalize method
        super(FunRandomDomainTooltipView, self)._finalize()
        # Releasing the caught sub-mode
        self.releaseSubMode()

