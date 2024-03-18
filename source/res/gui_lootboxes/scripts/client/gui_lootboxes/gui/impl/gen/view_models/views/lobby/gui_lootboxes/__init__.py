from gui.impl.gen.view_models.views.lobby.gui_lootboxes.loot_box_purchase_view_model import LootBoxPurchaseViewModel

class LootBoxPurchaseViewModel(ViewModel):

    def __init__(self, type, price):
        super(LootBoxPurchaseViewModel, self).__init__()
        self._type = type
        self._price = price

    @property
    def type(self):
        return self._type

    @property
    def price(self):
        return self._price

    def purchase(self):
        # code to purchase a loot box
        pass
