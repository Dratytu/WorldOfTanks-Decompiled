# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/lobby/feature/tooltips/rest_reward_tooltip_view.py
from armory_yard.gui.shared.bonus_packers import get_armory_yard_buy_view_packer
from frameworks.wulf import ViewSettings
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.rest_reward_tooltip_view_model import RestRewardTooltipViewModel
from gui.impl.gen import R
from gui.impl.lobby.common.view_helpers import pack_bonus_model_and_tooltip_data
from gui.impl.pub import ViewImpl

class RestRewardTooltipView(ViewImpl):
    __slots__ = ('__rewards',)

    def __init__(self, rewards):
        settings = ViewSettings(R.views.armory_yard.lobby.feature.tooltips.RestRewardTooltipView())
        settings.model = RestRewardTooltipViewModel()
        self.__rewards = rewards
        super().__init__(settings)

    @property
    def view_model(self):
        return super().getViewModel()

    def _onLoading(self, *args, **kwargs):
        super()._onLoading()
        with self.view_model.transaction() as vm:
            rewards_model = vm.getRewards()
            pack_bonus_model_and_tooltip_data(self.__rewards, rewards_model, packer=get_armory_yard_buy_view_packer())
            rewards_model.invalidate()
