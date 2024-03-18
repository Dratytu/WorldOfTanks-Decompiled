# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/team_model.py

# This script defines a ViewModel for a team in a lobby for the Battle Royale game mode.
# ViewModels are used in the MVVM architectural pattern to separate the graphical user
# interface from the business logic. They serve as a data container for the view and
# handle user interactions.

from frameworks.wulf import Array  # Importing Array from the wulf framework, used for arrays of ViewModels
from frameworks.wulf import ViewModel  # Importing ViewModel from the wulf framework, base class for all ViewModels
from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_model import UserModel  # Importing UserModel, used for team member representation

class TeamModel(ViewModel):
    # TeamModel is a ViewModel representing a team in the lobby.

    def __init__(self, properties=2, commands=0):
        # Initializes the TeamModel with the given properties and commands.
        # Properties are the data fields of the ViewModel, and commands are the
        # actions that can be performed on the ViewModel.

        super(TeamModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        # Returns the unique identifier of the team.

        return self._getNumber(0)

    def setId(self, value):
        # Sets the unique identifier of the team.

        self._setNumber(0, value)

    def getUsers(self):
        # Returns the list of users in the team.

        return self._getArray(1)

    def setUsers(self, value):
        # Sets the list of users in the team.

        self._setArray(1, value)

    @staticmethod
    def getUsersType():
        # Returns the type of elements in the users array
