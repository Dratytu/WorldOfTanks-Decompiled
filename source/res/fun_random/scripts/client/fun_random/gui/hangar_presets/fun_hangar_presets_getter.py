# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/hangar_presets/fun_hangar_presets_getter.py

# Import necessary constants and helper functions/classes
from constants import QUEUE_TYPE
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from gui.hangar_presets.hangar_presets_getters import BasePresetsGetter

# Define the FunRandomPresetsGetter class, which inherits from BasePresetsGetter and FunSubModesWatcher
class FunRandomPresetsGetter(BasePresetsGetter, FunSubModesWatcher):
    # Declare a slot for the __subModesPresets instance variable
    __slots__ = ('__subModesPresets',)
    
    # Set the _QUEUE_TYPE class variable to QUEUE_TYPE.FUN_RANDOM
    _QUEUE_TYPE = QUEUE_TYPE.FUN_RANDOM

    def __init__(self, config):
        # Call the constructor of the superclass with the provided config
        super(FunRandomPresetsGetter, self).__init__(config)
        
        # Initialize the __subModesPresets instance variable with the modes dict from the config, filtered by _QUEUE_TYPE
        self.__subModesPresets = config.modes[self._QUEUE_TYPE]

    @hasDesiredSubMode()
    def getPreset(self):
        # Get the desired submode implementation
        desiredSubModeImpl = self.getDesiredSubMode().getSubModeImpl()
        
        # Return the preset from the _presets dict using the key from the __subModesPresets dict corresponding to the desired submode implementation
        return self._presets.get(self.__subModesPresets.get(desiredSubModeImpl))

