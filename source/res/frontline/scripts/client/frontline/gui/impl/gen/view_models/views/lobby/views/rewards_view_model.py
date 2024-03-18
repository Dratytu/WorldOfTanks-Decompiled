# frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/rewards_view_model.py

# This class, RewardsViewModel, is a ViewModel for the rewards view in the frontline lobby.
# It is initialized with 5 properties and 1 command.
class RewardsViewModel(ViewModel):

    # The __slots__ attribute is used to save memory by preventing the creation of a dictionary for storing instance variables.
    # It also provides a way to explicitly declare instance variables, which can make the class definition easier to read.
    __slots__ = ('onClaimRewards',)

    def __init__(self, properties=5, commands=1):
        # Initialize the ViewModel with the given properties and commands.
        super(RewardsViewModel, self).__init__(properties=properties, commands=commands)

    # frontlineState: str - The current state of the frontline.
    def getFrontlineState(self):
        return self._getString(0)

    def setFrontlineState(self, value):
        self._setString(0, value)

    # selectableRewardsCount: int - The number of rewards that can still be selected.
    def getSelectableRewardsCount(self):
        return self._getNumber(1)

    def setSelectableRewardsCount(self, value):
        self._setNumber(1, value)

    # frontlineLevel: int - The current level of the frontline.
    def getFrontlineLevel(self):
        return self._getNumber(2)

    def setFrontlineLevel(self, value):
        self._setNumber(2, value)

    # isBattlePassComplete: bool - A flag indicating whether the battle pass is complete.
    def getIsBattlePassComplete(self):
        return self._getBool(3)

    def setIsBattlePassComplete(self, value):
        self._setBool(3, value)

    # rewards: List[FrontlineLvlRangeRewards] - A list of rewards for the current frontline level.
    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)

    # Static method for getting the type of the rewards property.
    # This is used to ensure that the correct type of object is added to the rewards list.
    @staticmethod
    def getRewardsType():
        return FrontlineLvlRangeRewards

    def _initialize(self):
        # Initialize the ViewModel with the default properties and commands.
        super(RewardsViewModel, self)._initialize()
        self._addStringProperty('frontlineState', '')
        self._addNumberProperty('selectableRewardsCount', 0)
        self._addNumberProperty('frontlineLevel', 0)
        self._addBoolProperty('isBattle
