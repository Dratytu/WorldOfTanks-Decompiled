# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/dialogs/sub_views/footer/br_single_price_footer.py

# Import necessary modules and classes
from battle_royale.gui.impl.dialogs import CurrencyTypeExtended
from gui.impl.dialogs.sub_views.common.single_price import SinglePrice
from gui.impl.gen import R  # Resource generator for dialogs
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize  # Enum for currency size


# Define the BRSinglePriceFooter class, which inherits from SinglePrice
class BRSinglePriceFooter(SinglePrice):
    # Declare an empty __slots__ attribute to improve memory usage and prevent the creation of dictionary for each instance
    __slots__ = ()
    
    # Define a class variable for the dynamic layout accessor
    _LAYOUT_DYN_ACCESSOR = R.views.dialogs.sub_views.footer.BRSinglePriceFooter
    
    def __init__(self, text, price, size=CurrencySize.SMALL, layoutID=None):
        # Call the constructor of the superclass, passing the required arguments and keyword arguments
        super(BRSinglePriceFooter, self).__init__(text, price, size, layoutID, CurrencyTypeExtended)
