# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/battle_queue.py

# Import necessary modules and classes
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.Scaleform.daapi.view.lobby.battle_queue import RandomQueueProvider
from gui.impl import backport

# Define the FunRandomQueueProvider class, which inherits from RandomQueueProvider,
# FunAssetPacksMixin, and FunSubModesWatcher
class FunRandomQueueProvider(RandomQueueProvider, FunAssetPacksMixin, FunSubModesWatcher):

    # Implement the getIconPath method to return the path of the icon
    def getIconPath(self, iconlabel):
        # Use backport.image to get the image path based on the provided image label
        # and the root of the resource for the battle type of the fun random mode
        return backport.image(self.getModeIconsResRoot().battle_type.c_136x136.fun_random())

    # Implement the getTitle method to return the title of the queue
    def getTitle(self, guiType):
        # Call the private __getTitle method or return the user name of the fun random mode
        return self.__getTitle() or self.getModeUserName()

    # Implement the processQueueInfo method to process the queue information
    def processQueueInfo(self, qInfo):
        # Call the superclass method to process the queue information
        super(FunRandomQueueProvider, self).processQueueInfo(qInfo or {})

    # Implement the _doRequestQueueInfo method to request queue information
    @hasDesiredSubMode()
    def _doRequestQueueInfo(self, currPlayer):
        # Call the superclass method to request queue information
        super(FunRandomQueueProvider, self)._doRequestQueueInfo(currPlayer)

    # Implement the _getRequestQueueInfoParams method to get request queue info
