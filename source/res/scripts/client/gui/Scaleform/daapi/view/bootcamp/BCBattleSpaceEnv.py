# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSpaceEnv.py

# Import the necessary modules for working with sounds and ambients
from gui.sounds.ambients import BattleSpaceEnv, NoMusic

# Define the BCBattleSpaceEnv class, which inherits from the BattleSpaceEnv class
class BCBattleSpaceEnv(BattleSpaceEnv):

    # Override the 'stop' method from the parent class
    def stop(self):
        # Set the music attribute to an instance of the NoMusic class
        self._music = NoMusic()
        
        # Call the _onChanged method
        self._onChanged()
        
        # Call the 'stop' method of the parent class
        super(BCBattleSpaceEnv, self).stop()

    # Override the '_setAfterBattleAmbient' method from the parent class
    def _setAfterBattleAmbient(self):
        # This method currently does not contain any code, so it does nothing
        pass

