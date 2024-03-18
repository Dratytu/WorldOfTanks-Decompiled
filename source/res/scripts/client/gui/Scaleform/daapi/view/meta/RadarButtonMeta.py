# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadarButtonMeta.py

import sys # Imported for print-method in onClick()
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent # Inherited class for handling DAAPI-related functionality

class RadarButtonMeta(BaseDAAPIComponent):
    """ Meta-class for the RadarButton component in the Scaleform GUI framework. """

    def onClick(self):
        """
        Overridden method for handling click events on the radar button.
        :return: None
        """
        sys.stdout.write("onClick() called. This method should be overridden in a subclass to handle click events.\n")
        self._printOverrideError('onClick')

    def as_initS(self, keyCode, sfKeyCode, iconPath, tooltipText, isReplay):
        """
        Method for initializing the radar button with specific parameters.
        :param keyCode: The key code for the radar button.
        :param sfKeyCode: The SF key code for the radar button.
        :param iconPath: The path to the icon for the radar button.
        :param tooltipText: The text for the tooltip of the radar button.
        :param isReplay: A boolean indicating whether the game is in replay mode.
        :return: An ActionScript value representing the initialization data.
        """
        return self.flashObject.as_init(keyCode, sfKeyCode, iconPath, tooltipText, isReplay) if self._isDAAPIInited() else None

    def as_setCoolDownTimeS(self, duration, baseTime, startTime, animation):
        """
        Method for setting the cooldown time for the radar button.
        :param duration: The total duration of the cooldown.
        :param baseTime: The base time for the cooldown.
        :param startTime: The start time for the cooldown.
