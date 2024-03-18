class ArmoryYardLevelModel(wulf.ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ArmoryYardLevelModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(ArmoryYardLevelModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addArrayProperty('rewards', None)
        self._addBooleanProperty('isExpanded', False)
