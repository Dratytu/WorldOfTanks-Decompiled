# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyalePlayersPanelMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the BattleRoyalePlayersPanelMeta class, which inherits from BaseDAAPIComponent
class BattleRoyalePlayersPanelMeta(BaseDAAPIComponent):

    # Define the switchToPlayer method, which takes a single argument: vehicleID
    def switchToPlayer(self, vehicleID):
        # Print an override error message, indicating that this method should not be called directly
        self._printOverrideError('switchToPlayer')

    # Define the as_setPlayersDataS method, which takes two arguments: data and lostIndex
    def as_setPlayersDataS(self, data, lostIndex):
        # If the DAAPI is initialized, call the as_setPlayersData method on the flashObject with the provided data and lostIndex
        return self.flashObject.as_setPlayersData(data, lostIndex) if self._isDAAPIInited() else None

    # Define the as_setSeparatorVisibilityS method, which takes a single argument: isVisible
    def as_setSeparatorVisibilityS(self, isVisible):
        # If the DAAPI is initialized, call the as_setSeparatorVisibility method on the flashObject with the provided isVisible
        return self.flashObject.as_setSeparatorVisibility(isVisible) if self._isDAAPIInited() else None

