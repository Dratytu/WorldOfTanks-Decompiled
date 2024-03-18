# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/hangar/fun_random_entry_point.py

# Import necessary modules
from frameworks.wulf import ViewFlags  # Wulf framework's ViewFlags module is used for setting view flags
from fun_random.gui.impl.lobby.feature.fun_random_entry_point_view import FunRandomEntryPointView  # Importing the custom view class for the Fun Random entry point
from gui.Scaleform.daapi.view.meta.FunRandomEntryPointMeta import FunRandomEntryPointMeta  # Importing the meta class for the Fun Random entry point

# Define the FunRandomEntryPoint class
class FunRandomEntryPoint(FunRandomEntryPointMeta):

    # Initialize the FunRandomEntryPoint class with necessary parameters
    def __init__(self, auth_id: int, auth_token: str, settings: dict, fun_random_settings: dict, *args, **kwargs):
        super(FunRandomEntryPoint, self).__init__(*args, **kwargs)
        self._authId = auth_id
        self._authToken = auth_token
        self._settings = settings
        self._funRandomSettings = fun_random_settings

    # Override the onEntry method
    def onEntry(self):
        # Initialize the Fun Random entry point view
        self.funRandomEntryPointView = FunRandomEntryPointView(self._authId, self._authToken, self._settings, self._funRandomSettings, flags=ViewFlags.LOBBY_TOP_WINDOW)
        self.as_setFunRandomEntryPointViewS(self.funRandomEntryPointView.as_view())

