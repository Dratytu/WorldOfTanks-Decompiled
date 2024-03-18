# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/BoosterInfoWindow.py

# Import necessary modules and classes
from gui.Scaleform import MENU # Importing MENU constant from gui.Scaleform package
from gui.Scaleform.daapi.view.meta.BoosterInfoMeta import BoosterInfoMeta # Inheriting from BoosterInfoMeta class
from gui.Scaleform.framework.entities.View import View # Inheriting from View class
from helpers import dependency # Using dependency injection helper
from helpers.i18n import makeString as _ms # Importing makeString function for internationalization
from skeletons.gui.goodies import IGoodiesCache # Dependency for IGoodiesCache interface

# Class definition for BoosterInfoWindow
class BoosterInfoWindow(View, BoosterInfoMeta, dependency.Dependency):

    # Inject IGoodiesCache implementation
    _goodiesCache = dependency.descriptor(IGoodiesCache)

    # Initializer for BoosterInfoWindow
    def __init__(self):
        super(BoosterInfoWindow, self).__init__()

    # Override show method
    def show(self, boosterCD):
        """
        :param boosterCD: Booster CD key
        :type boosterCD: str
        """
        # Set booster data using the provided CD key
        self.setBoosterData(boosterCD)
        # Display the booster info window
        super(BoosterInfoWindow, self).show()

    # Method to set booster data
    def setBoosterData(self, boosterCD):
        """
        Set booster data using the provided CD key.
        :param boosterCD: Booster CD key
        :type boosterCD: str
        """
        # Get booster data from the cache using the CD key
        boosterData = self._goodiesCache.getBoosterByCDKey(boosterCD)
        # Set booster data in the view
        self.
