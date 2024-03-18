# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/BootcampAccount.py

import cPickle
import AccountCommands
import BattleReplay
from Account import PlayerAccount
from PlayerEvents import g_playerEvents as events
from constants import QUEUE_TYPE
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP
from bootcamp.Bootcamp import g_bootcamp
from bootcamp.BootCampEvents import g_bootcampEvents
from gui.game_loading.resources.consts import Milestones

# Subclass of PlayerAccount specifically for the Bootcamp mode
class PlayerBootcampAccount(PlayerAccount):

    # Called when the account becomes a player
    def onBecomePlayer(self):
        replayCtrl = BattleReplay.g_replayCtrl
        # Stop recording a replay if it's currently recording
        if replayCtrl.isRecording:
            replayCtrl.stop()
        # Call the superclass's onBecomePlayer method
        super(PlayerBootcampAccount, self).onBecomePlayer()
        # Set the Bootcamp's account to this account object
        if g_bootcamp is not None:
            g_bootcamp.setAccount(self)
        # Notify the BootcampEvents module that the account has become a player
        g_bootcampEvents.onBootcampBecomePlayer()
        # Show the action wait window
        g_bootcamp.showActionWaitWindow()
        return

    # Called when the account becomes a non-player
    def onBecomeNonPlayer(self):
        # Call the superclass's onBecomeNonPlayer method
        super(PlayerBootcampAccount, self).onBecomeNonPlayer()
        # Notify the BootcampEvents module that the account has become a non-player
        g_bootcampEvents.onBootcampBecomeNonPlayer()
        # Hide the action wait window
        g_bootcamp.hideActionWaitWindow()
        # Set the Bootcamp's account to None
        if g_bootcamp is not None:
            g_bootcamp.setAccount(None)
        return

    # Static method to finish the Bootcamp
    @staticmethod
    def finishBootcamp():
        LOG_DEBUG_DEV_BOOTCAMP('finishBootcamp called')
        # Call the Bootcamp module's finishBootcamp method
        g_bootcamp.finishBootcamp()

    # Called when the account's GUI is shown
    def showGUI(self, ctx):
        LOG_DEBUG_DEV_BOOTCAMP('showGUI called')
        # Hide the action wait window
        g_bootcamp.hideActionWaitWindow()
        # Unpickle the context data
        ctx = cPickle.loads(ctx)
        # Get the GUI context from the context data
        guiCtx = ctx['gui']
        # Call the lobby context's onAccountShowGUI method with the GUI context
        self.lobbyContext.onAccountShowGUI(guiCtx)
        # Initialize time correction with the GUI context
        self._initTimeCorrection(guiCtx)
        # Get the Bootcamp context from the context data
        bootcampCtx = ctx['bootcamp']
        # Set the account's database ID
        self.databaseID = bootcampCtx['databaseID']
        # Set the account's current lesson number
        currentLesson = bootcampCtx['lessonNum']
        # Set the account's isBattleLesson flag
        isBattleLesson = bootcampCtx['isBattleLesson']
        # Set the Bootcamp's account to this account object
        g_bootcamp.setAccount(self)
        # Set the Bootcamp's context to the Bootcamp context
        g_bootcamp.setContext(bootcampCtx)
        # Set the isPlayerEntityChanging flag to False
        events.isPlayerEntityChanging = False
        # Notify the BootcampEvents module that the account's GUI is shown
