# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_results/components.py

# Importing RegularArenaFullNameItem from the common module of the battle_results package
# and makeArenaFullName function from the same common module
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from gui.battle_results.components.common import RegularArenaFullNameItem, makeArenaFullName

# Defining a new class FunRandomArenaFullNameItem that inherits from RegularArenaFullNameItem and FunAssetPacksMixin
class FunRandomArenaFullNameItem(RegularArenaFullNameItem, FunAssetPacksMixin):
    # Declaring an empty __slots__ attribute to prevent the creation of a __dict__ object for each instance
    __slots__ = ()

    # Defining the _convert method that takes three arguments: self, record, and reusable
    def _convert(self, record, reusable):
        # Extracting the arenaType attribute from the reusable object
        arenaType = reusable.common.arenaType
        # Calling the makeArenaFullName function with two arguments: arenaType.getName() and self.getModeUserName()
        # and returning the result
        return makeArenaFullName(arenaType.getName(), self.getModeUserName())
