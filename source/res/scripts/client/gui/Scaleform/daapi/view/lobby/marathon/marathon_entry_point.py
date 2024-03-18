# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/marathon/marathon_entry_point.py

# Import necessary modules
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.MarathonEntryPointMeta import MarathonEntryPointMeta
from gui.impl.lobby.marathon.marathon_entry_point import MarathonEntryPoint

# Define the MarathonEntryPointWrapper class, which inherits from MarathonEntryPointMeta
class MarathonEntryPointWrapper(MarathonEntryPointMeta):

    # Define the _makeInjectView method
    def _makeInjectView(self):
        # Create an instance of the MarathonEntryPoint class with the ViewFlags.VIEW flag
        self.__view = MarathonEntryPoint(flags=ViewFlags.VIEW)
        
        # Return the created instance
        return self.__view
