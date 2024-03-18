# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSpaceEnv.py

# Import the necessary modules for working with sounds and ambients
from gui.sounds.ambients import BattleSpaceEnv, NoMusic  # Import the BattleSpaceEnv class and the NoMusic class from the gui.sounds.ambients module

# Define the BCBattleSpaceEnv class, which inherits from the BattleSpaceEnv class
class BCBattleSpaceEnv(BattleSpaceEnv):

    # Override the 'stop' method from the parent class
    def stop(self):
        # Set the music attribute to an instance of the NoMusic class
        # This stops any music that was previously playing
        self._music = NoMusic()

        # Call the _onChanged method
        # This method is likely used to notify any listeners that the ambient sound has changed
        self._onChanged()

        # Call the 'stop' method of the parent class
        # This stops any ambient sounds that were previously playing
        super(BCBattleSpaceEnv, self).stop()

    # Override the '_setAfterBattleAmbient' method from the parent class
    def _setAfterBattleAmbient(self):
        # This method currently does not contain any code, so it does nothing
        # However, it is likely that this method is intended to be used to set the ambient sound after a battle has ended
        pass
