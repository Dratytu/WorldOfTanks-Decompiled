# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/impl/gen/view_models/views/lobby/views/battle_quests_model.py

# This file defines the BattleQuestsModel class, which is a subclass of ViewModel.
# ViewModel is a base class for all view models in the framework, providing
# properties and commands support.

from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class BattleQuestsModel(ViewModel):
    # BattleQuestsModel is a custom view model for managing battle quests in the lobby.
    # It has several properties to store and manage quest-related data.

    def __init__(self, properties=3, commands=0):
        # Initialize the ViewModel with the given properties and commands.
        super(BattleQuestsModel, self).__init__(properties=properties, commands=commands)

    def getTasksBattle(self):
        # Returns the list of tasks for the current battle.
        return self._getArray(0)

    def setTasksBattle(self, value):
        # Sets the list of tasks for the current battle.
        self._setArray(0, value)

    @staticmethod
    def getTasksBattleType():
        # Returns the type of the tasksBattle property, which is an Array of QuestModel instances.
        return QuestModel

    def getCurrentTimerDate(self):
        # Returns the current timer date for the battle quests.
        return self._getNumber(1)

    def setCurrentTimerDate(self, value):
        # Sets the current timer date for the battle quests.
        self._setNumber(1, value)

    def getMissionsCompletedVisited(self):
        # Returns the list of completed and visited missions.
        return self._getArray(2)

    def setMissionsCompletedVisited(self, value):
        # Sets the list of completed and
