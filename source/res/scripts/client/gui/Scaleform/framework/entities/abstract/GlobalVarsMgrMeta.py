# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GlobalVarsMgrMeta.py

from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent  # Importing BaseDAAPIComponent to inherit its properties and methods

class GlobalVarsMgrMeta(BaseDAAPIComponent):
    """
    A meta class for the GlobalVarsMgr component, which provides access to various global variables and flags used in the game.
    """

    def isDevelopment(self):
        """
        Returns a boolean indicating whether the game is currently in development mode.
        """
        self._printOverrideError('isDevelopment')  # Prints an error message if this method is overridden without proper implementation

    def isShowLangaugeBar(self):
        """
        Returns a boolean indicating whether the language bar is currently visible.
        """
        self._printOverrideError('isShowLangaugeBar') 

    def isShowServerStats(self):
        """
        Returns a boolean indicating whether server stats are currently visible.
        """
        self._printOverrideError('isShowServerStats') 

    def isChina(self):
        """
        Returns a boolean indicating whether the game is running in the Chinese region.
        """
        self._printOverrideError('isChina') 

    def isKorea(self):
        """
        Returns a boolean indicating whether the game is running in the Korean region.
        """
        self._printOverrideError('isKorea') 

    def isTutorialRunning(self, tutorialID):
        """
        Returns a boolean indicating whether a specific tutorial is currently running.

        :param tutorialID: The ID of the tutorial.
        """
        self._printOverrideError('isTutorialRunning') 

    def isRoamingEnabled(self):
        """
        Returns a boolean indicating whether roaming is currently enabled.
        """
        self._printOverrideError('isRoamingEnabled') 

    def isInRoaming(self):
        """
        Returns a boolean indicating whether the player is currently in a roaming state.
        """
        self._printOverrideError('isInRoaming') 

    def isFreeXpToTankman(self):
        """
        Returns a boolean indicating whether free XP can be converted to crew XP.
        """
        self._printOverrideError('isFreeXpToTankman') 

    def getLocaleOverride(self):
        """
        Returns the currently overridden locale, if any.
        """
        self._printOverrideError('getLocaleOverride') 

    def isFortificationAvailable(self):
        """
        Returns a boolean indicating whether fortification is available.
        """
