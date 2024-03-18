# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/royale_models.py

# Import the namedtuple function from the collections module
from collections import namedtuple

# Import the GameSeason class from the season_common module
from season_common import GameSeason

# Define a new namedtuple called BattleRoyaleCycle with the fields: ID, status, startDate, endDate, ordinalNumber, announceOnly
class BattleRoyaleCycle(namedtuple('BattleRoyaleCycle', 'ID, status, startDate, endDate, ordinalNumber, announceOnly')):

    # Define a custom comparison method for the namedtuple
    def __cmp__(self, other):
        # Compare the ID fields of the two namedtuples
        return cmp(self.ID, other.ID)

    # Define a method to get the user-friendly name for the cycle
    def getUserName(self):
        # Return the ordinalNumber field as a string
        return str(self.ordinalNumber)

    # Define a method to get the epic cycle number for the cycle
    def getEpicCycleNumber(self):
        # Return the ordinalNumber field
        return self.ordinalNumber


# Define a new class called BattleRoyaleSeason that inherits from the GameSeason class
class BattleRoyaleSeason(GameSeason):

    # Override the _buildCycle method to return a new BattleRoyaleCycle instance
    def _buildCycle(self, idx, status, number, rawData):
        # Return a new BattleRoyaleCycle instance with the given arguments
        return BattleRoyaleCycle(idx, status, rawData['start'], rawData['end'], number, bool(rawData.get('announce', False)))
