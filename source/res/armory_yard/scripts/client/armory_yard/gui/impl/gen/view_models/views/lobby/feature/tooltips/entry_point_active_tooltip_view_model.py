# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/tooltips/entry_point_active_tooltip_view_model.py

from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.armory_yard_tooltip_chapter_model import ArmoryYardTooltipChapterModel  # Import for the Chapter model

class EntryPointActiveTooltipViewModel(ViewModel):
    # Initialize the view model with default properties and no commands
    def __init__(self, properties=5, commands=0):
        super(EntryPointActiveTooltipViewModel, self).__init__(properties=properties, commands=commands)

    # Getter for the number of quests in progress
    def getQuestsInProgress(self):
        return self._getNumber(0)

    # Setter for the number of quests in progress
    def setQuestsInProgress(self, value):
        self._setNumber(0, value)

    # Getter for the end timestamp of the active entry
    def getEndTimestamp(self):
        return self._getNumber(1)

    # Setter for the end timestamp of the active entry
    def setEndTimestamp(self, value):
        self._setNumber(1, value)

    # Getter for the array of chapter models
    def getChapters(self):
        return self._getArray(2)

    # Setter for the array of chapter models
    def setChapters(self, value):
        self._setArray(2, value)

    # A static method to get the type of the chapter models
    @staticmethod
    def getChaptersType():
        return ArmoryYardTooltipChapterModel

    # Getter for the number of received tokens
    def getReceivedTokens(self):
        return self._getNumber(3)

    # Setter for the number of received tokens
    def setReceivedTokens(self, value):
        self._setNumber(3, value)

    # Getter for the total number of tokens
    def getTotalTokens(self):
        return self._getNumber(4)

    # Setter for the total number of tokens
    def setTotalTokens(self, value):
        self._setNumber(4, value)

    # Initialize the properties of the view model
    def _initialize(self):
        super(EntryPointActiveTooltipViewModel, self)._initialize()
        self._addNumberProperty('questsInProgress', 0)  # Initialize the number of quests in progress
        self._addNumberProperty('endTimestamp', 0)  # Initialize the end timestamp of the active entry
        self._addArrayProperty('chapters', Array())  # Initialize the array of chapter models
