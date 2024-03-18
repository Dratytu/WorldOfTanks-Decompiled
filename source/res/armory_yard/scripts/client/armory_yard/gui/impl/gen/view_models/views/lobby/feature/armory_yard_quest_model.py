# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_quest_model.py

import super
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel  # Importing QuestModel class from a common missions package

# Defining ArmoryYardQuestModel class, which inherits from QuestModel class
class ArmoryYardQuestModel(QuestModel):
    # Defining a list of properties and commands for the class
    __slots__ = ()

    # Initializing the class with default properties and commands
    def __init__(self, properties=13, commands=0):
        # Calling the constructor of the parent class with the given properties and commands
        super(ArmoryYardQuestModel, self).__init__(properties=properties, commands=commands)

    # A getter method for the 'chapterId' property
    def getChapterId(self):
        return self._getNumber(11)

    # A setter method for the 'chapterId' property
    def setChapterId(self, value):
        self._setNumber(1
