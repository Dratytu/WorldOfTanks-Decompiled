# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_entry_point_inject.py

# Import necessary classes and functions.
from battle_royale.gui.impl.lobby.views.battle_royale_entry_point import BattleRoyaleEntryPoint
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta

# Define the BattleRoyaleEntryPointInject class that inherits from ResizableEntryPointMeta.
class BattleRoyaleEntryPointInject(ResizableEntryPointMeta):

    # Define the isSingle method that takes a value as an argument.
    def isSingle(self, value):
        # Check if the __view attribute exists.
        if self.__view:
            # Call the setIsSingle method of the __view attribute with the provided value.
            self.__view.setIsSingle(value)

    # Define the _makeInjectView method.
    def _makeInjectView(self):
        # Create a new instance of the BattleRoyaleEntryPoint class with the flags argument set to ViewFlags.VIEW.
        self.__view = BattleRoyaleEntryPoint(flags=ViewFlags.VIEW)
        # Return the newly created __view instance.
        return self.__view

