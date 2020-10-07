# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_awards_view_model.py
from frameworks.wulf import Array
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.common_view_model import CommonViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BattlePassAwardsViewModel(CommonViewModel):
    __slots__ = ('onBuyClick', 'onDeviceSelectClick')
    BUY_BATTLE_PASS_REASON = 'buyBattlePassReason'
    BUY_BATTLE_PASS_LEVELS_REASON = 'buyBattlePassLevelsReason'
    SELECT_TROPHY_DEVICE_REASON = 'selectTrophyDeviceReason'
    DEFAULT_REASON = 'defaultReason'

    def __init__(self, properties=16, commands=3):
        super(BattlePassAwardsViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainRewards(self):
        return self._getViewModel(7)

    @property
    def additionalRewards(self):
        return self._getViewModel(8)

    def getPreviousLevel(self):
        return self._getNumber(9)

    def setPreviousLevel(self, value):
        self._setNumber(9, value)

    def getReason(self):
        return self._getString(10)

    def setReason(self, value):
        self._setString(10, value)

    def getIsFinalReward(self):
        return self._getBool(11)

    def setIsFinalReward(self, value):
        self._setBool(11, value)

    def getBadgeTooltipId(self):
        return self._getString(12)

    def setBadgeTooltipId(self, value):
        self._setString(12, value)

    def getIsChooseDeviceEnabled(self):
        return self._getBool(13)

    def setIsChooseDeviceEnabled(self, value):
        self._setBool(13, value)

    def getIsNeedToShowOffer(self):
        return self._getBool(14)

    def setIsNeedToShowOffer(self, value):
        self._setBool(14, value)

    def getWideRewardsIDs(self):
        return self._getArray(15)

    def setWideRewardsIDs(self, value):
        self._setArray(15, value)

    def _initialize(self):
        super(BattlePassAwardsViewModel, self)._initialize()
        self._addViewModelProperty('mainRewards', UserListModel())
        self._addViewModelProperty('additionalRewards', UserListModel())
        self._addNumberProperty('previousLevel', 0)
        self._addStringProperty('reason', 'defaultReason')
        self._addBoolProperty('isFinalReward', False)
        self._addStringProperty('badgeTooltipId', '')
        self._addBoolProperty('isChooseDeviceEnabled', True)
        self._addBoolProperty('isNeedToShowOffer', False)
        self._addArrayProperty('wideRewardsIDs', Array())
        self.onBuyClick = self._addCommand('onBuyClick')
        self.onDeviceSelectClick = self._addCommand('onDeviceSelectClick')
