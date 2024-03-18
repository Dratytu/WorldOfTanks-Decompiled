# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/SoundManagerMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities.BaseDAAPIComponent module
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the SoundManagerMeta class that inherits from BaseDAAPIComponent
class SoundManagerMeta(BaseDAAPIComponent):

    # Define the soundEventHandler method
    def soundEventHandler(self, group, state, type, id):
        # Print an error message indicating that the method has been overridden
        # This is useful for debugging and ensuring that the method is being called correctly
        self._printOverrideError('soundEventHandler')

