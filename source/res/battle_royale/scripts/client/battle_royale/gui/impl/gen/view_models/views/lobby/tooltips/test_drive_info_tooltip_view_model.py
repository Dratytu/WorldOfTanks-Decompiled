# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/test_drive_info_tooltip_view_model.py
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.rent_price_model import RentPriceModel

class TestDriveInfoTooltipViewModel(ViewModel):
    """View model for the tooltip that displays information about the test drive feature in the lobby."""
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        """Initializes the view model with 2 properties and 0 commands."""
        super(TestDriveInfoTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def price(self):
        """Returns the view model for the price of the test drive."""
        return self._getViewModel(0)

    @static
