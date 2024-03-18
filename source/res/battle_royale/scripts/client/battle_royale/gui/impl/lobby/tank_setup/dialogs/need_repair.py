# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/tank_setup/dialogs/need_repair.py

# Import necessary modules and constants
from constants import Configs
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import NeedRepairMainContent
from gui.impl.lobby.tank_setup.dialogs.need_repair import NeedRepair
from helpers import dependency, server_settings
from skeletons.gui.lobby_context import ILobbyContext

# Define a new class NeedRepairMainContentBattleRoyale that inherits from NeedRepairMainContent
class NeedRepairMainContentBattleRoyale(NeedRepairMainContent):

    # Override the onLoading method
    def onLoading(self, *args, **kwargs):
        # Call the superclass's onLoading method
        super(NeedRepairMainContentBattleRoyale, self).onLoading(*args, **kwargs)
        # Begin a transaction on the view model
        with self._viewModel.transaction() as model:
            # Set the repair percentage on the model
            model.setRepairPercentage(self._repairPercentage)
            # Set the free auto repair to False
            model.setFreeAutoRepair(False)

# Define a new class NeedRepairBattleRoyale that inherits from NeedRepair
class NeedRepairBattleRoyale(NeedRepair):
    # Inject the lobby context dependency
    __lobbyContext = dependency.descriptor(ILobbyContext)

    # Initialize the class
    def _initialize(self, *args, **kwargs):
        # Call the superclass's initialization method
        super(NeedRepairBattleRoyale, self)._initialize(*args, **kwargs)
        # Register a callback for server settings changes
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged

    # Finalize the class
    def _finalize(self):
        # Unregister the callback for server settings changes
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        # Call the superclass's finalization method
        super(NeedRepairBattleRoyale, self)._finalize()

    # Decorate the onServerSettingsChanged method with the serverSettingsChangeListener decorator
    @server_settings.serverSettingsChangeListener(Configs.BATTLE_ROYALE_CONFIG.value)
   
