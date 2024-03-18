# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/page.py

# Import necessary modules
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES

# Define constants for epic random classic components
_EPIC_RANDOM_CLASSICS_COMPONENTS = COMMON_CLASSIC_CONFIG

# Define constants for epic random extended components
_EPIC_RANDOM_EXTENDED_COMPONENTS = EXTENDED_CLASSIC_CONFIG

# Subclass ClassicPage to create EpicRandomPage
class EpicRandomPage(ClassicPage):

    # Constructor for EpicRandomPage
    def __init__(self, components=None, external=None, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS):
        # If components are not provided, set them to epic random classics components
        # if replay is not playing, or epic random extended components if replay is playing
        if components is None:
            components = _EPIC_RANDOM_CLASSICS_COMPONENTS if self.sessionProvider.isReplayPlaying else _EPIC_RANDOM_EXTENDED_COMPONENTS
        # Call the constructor of the superclass with the provided components, external, and fullStatsAlias
        super(EpicRandomPage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        return

    # Called when battle loading starts
    def _onBattleLoadingStart(self):
        # Call the superclass's implementation of _onBattleLoadingStart
        super(EpicRandomPage, self)._onBattleLoadingStart()
        # If replay is not playing, enter gui control mode for battle loading
        if not self.sessionProvider.isReplayPlaying:
            self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.BATTLE_LOADING)

    # Called when battle loading finishes
   
