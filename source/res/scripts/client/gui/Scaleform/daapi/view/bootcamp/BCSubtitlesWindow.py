# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCSubtitlesWindow.py

# Import necessary modules
from bootcamp.subtitles.subtitles import SubtitlesBase
from tutorial.gui.Scaleform.pop_ups import TutorialWindow
from gui.Scaleform.daapi.view.meta.SubtitlesWindowMeta import SubtitlesWindowMeta

# Define the SubtitlesWindow class, which inherits from SubtitlesBase, SubtitlesWindowMeta, and TutorialWindow
class SubtitlesWindow(SubtitlesBase, SubtitlesWindowMeta, TutorialWindow):

    # onWindowClose method, called when the window is closed
    def onWindowClose(self):
        # Call the superclass's onWindowClose method
        super(SubtitlesWindow, self).onWindowClose()
        # Call the _onMouseClicked method with the argument 'closeID'
        self._onMouseClicked('closeID')
        # Call the _stop method
        self._stop()

    # _asShowSubtitle method, called to display a subtitle
    def _asShowSubtitle(self, subtitle):
        # Call the as_showSubtitleS method with the subtitle as an argument
        self.as_showSubtitleS(subtitle)

    # _asHideSubtitle method, called to hide the current subtitle
    def _asHideSubtitle(self):
        # Call the as_hideSubtitleS method
        self.as_hideSubtitleS()

    # _stop method, called to stop the subtitles
    def _stop(self):
        # Clear the content of the window
        self._content.clear()
        # If the tutorial object is not None
        if self._tutorial is not None:
            # Iterate through all effects in the _gui.effects object
            for _, effect in self._gui.effects.iterEffects():
                # If the effect is still running and associated with this window
                if effect.
