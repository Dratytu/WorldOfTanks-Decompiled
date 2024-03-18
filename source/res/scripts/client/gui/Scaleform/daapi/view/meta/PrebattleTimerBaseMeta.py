# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerBaseMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent # Importing BaseDAAPIComponent class from the Scaleform framework.

class PrebattleTimerBaseMeta(BaseDAAPIComponent):
    """
    Meta class for the PrebattleTimer component, which is responsible for displaying a countdown timer and other related information in the pre-battle UI.
    """

    def as_setTimerS(self, totalTime):
        """
        Sets the total time for the countdown timer.

        :param totalTime: The total time in seconds for the countdown timer.
        :return: An ActionScript message to be sent to the view component.
        """
        return self.flashObject.as_setTimer(totalTime) if self._isDAAPIInited() else None

    def as_setMessageS(self, msg):
        """
        Sets a message to be displayed in the pre-battle UI.

        :param msg: The message to be displayed.
        :return: An ActionScript message to be sent to the view component.
        """
        return self.flashObject.as_setMessage(msg) if self._isDAAPIInited() else None

    def as_hideAllS(self, useAnim):
        """
        Hides all UI elements in the pre-battle timer.

        :param useAnim: A flag indicating whether to use an animation when hiding the elements.
        :return: An ActionScript message to be sent to the view component.
        """
        return self.flashObject.as_hideAll(useAnim) if self._isDAAPIInited() else None

    def as_setWinConditionTextS(self, winCondition):
        """
        Sets the text for the win condition in the pre-battle UI.

        :param winCondition: The text to be displayed as the win condition.
        :return: An ActionScript message to be sent to
