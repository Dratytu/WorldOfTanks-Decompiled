# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/arena_info/arena_descrs.py

import BattleReplay
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from gui.battle_control.arena_info.arena_descrs import ArenaWithLabelDescription
from gui.impl import backport

class FunRandomArenaDescription(ArenaWithLabelDescription, FunAssetPacksMixin, FunSubModesWatcher):
    # isInvitationEnabled method checks if the invitation is enabled
    def isInvitationEnabled(self):
        replayCtrl = BattleReplay.g_replayCtrl
        # Return True if the replay is not playing, False otherwise
        return not replayCtrl.isPlaying

    # getBattleTypeIconPath method returns the path of the battle type icon
    def getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        # Get the icon resource and append the size folder and frame to it
        iconRes = self.getModeIconsResRoot().battle_type.dyn(sizeFolder).dyn(self.getFrameLabel())
        # If the icon resource exists, return its path using backport.image, otherwise return an empty string
        return backport.image(iconRes()) if iconRes.exists() else ''

    # getDescriptionString method returns the description string
    def getDescriptionString(self, isInBattle=True):
        # Call the private method __getDescriptionString and return its result or the mode user name
        return self.__getDescriptionString() or self.getModeUserName()

    # __getDescriptionString method returns the detailed user name of the battle sub mode
    @hasBattleSubMode(self, defReturn='')
    def __getDescriptionString(self):
        # Get the localized user name of the battle
