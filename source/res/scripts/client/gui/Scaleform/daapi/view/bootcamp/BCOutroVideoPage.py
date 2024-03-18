# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCOutroVideoPage.py

# Import necessary modules
from gui.Scaleform.daapi.view.bootcamp.BCVideoPage import BCVideoPage
from tutorial.gui.Scaleform.pop_ups import TutorialDialog
from uilogging.deprecated.decorators import loggerTarget, loggerEntry, simpleLog
from uilogging.deprecated.bootcamp.constants import BC_LOG_ACTIONS, BC_LOG_KEYS
from uilogging.deprecated.bootcamp.loggers import BootcampUILogger

# Define the BCOutroVideoPage class, which inherits from BCVideoPage and TutorialDialog
@loggerTarget(logKey=BC_LOG_KEYS.BC_OUTRO_VIDEO, loggerCls=BootcampUILogger)
class BCOutroVideoPage(BCVideoPage, TutorialDialog):

    # Define the default master volume for the video
    _DEFAULT_MASTER_VOLUME = 0.5

    # Define the cancel method, which is called when the user clicks the cancel button
    def cancel(self):
        # Call the _onMouseClicked method with the argument 'cancelID'
        self._onMouseClicked('cancelID')
        # Call the _onFinish method
        self._onFinish()

    # Define the _onDestroy method, which is called when the object is destroyed
    @simpleLog(action=BC_LOG_ACTIONS.SKIP_VIDEO)
    def _onDestroy(self):
        # Add a listener for the onDispose event
        self.onDispose += self.__onDispose
        # Clear the content of the video
        self._content.clear()
        # If the tutorial object is not None
        if self._tutorial is not None:
            # Iterate through all effects in the gui
            for _, effect in self._gui.effects.iterEffects():
                # If the effect is still running
                if effect.isStillRunning(self.uniqueName):
                    # Stop the effect
                    effect.stop(effectID=None)

