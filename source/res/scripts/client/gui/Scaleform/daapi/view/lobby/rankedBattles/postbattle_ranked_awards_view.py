# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/postbattle_ranked_awards_view.py

import SoundGroups  # Import the SoundGroups module for playing sounds
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES  # Import aliases for Ranked Battles
from gui.impl import backport  # Import backport module for text formatting
from gui.impl.gen import R  # Import R for accessing localized strings
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_OVERLAY_SOUND_SPACE  # Import RANKED_OVERLAY_SOUND_SPACE
from gui.ranked_battles.ranked_builders.postbattle_awards_vos import getVOsSequence  # Import getVOsSequence function
from gui.Scaleform.daapi.view.meta.RankedBattlesAwardsViewMeta import RankedBattlesAwardsViewMeta  # Import RankedBattlesAwardsViewMeta
from helpers import dependency  # Import dependency for managing dependencies
from skeletons.gui.game_control import IRankedBattlesController  # Import IRankedBattlesController from skeletons

class PostbattleRankedAwardsView(RankedBattlesAwardsViewMeta):
    # Declare the class with a dependency on IRankedBattlesController
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, ctx=None):
        super(PostbattleRankedAwardsView, self).__init__()
        # Initialize the awardsSequence and rankedInfo attributes with the provided context
        self.__awardsSequence = ctx['awardsSequence']
        self.__rankedInfo = ctx['rankedInfo']

    def closeView(self):
        # Close the view and destroy it
        self.__close()

    def onSoundTrigger(self, triggerName):
        # Play the specified sound using SoundGroups
        SoundGroups.g_instance.playSound2D(triggerName)

    def _populate(self):
        # Override the _populate method to set data for the view
        super(PostbattleRankedAwardsView, self)._populate()
        vosSequence = getVOsSequence(
            self.__awardsSequence,
            self.__rankedController.getRanksChain(
                min(self.__awardsSequence, key=lambda x: x.rankID).rankID if self.__awardsSequence else 0,
                max(self.__awardsSequence, key=lambda x: x.rankID).rankID + 1 if self.__awardsSequence else 0
            ),
            self.__rankedInfo
        )
        self.as_setDataS({
            'vosSequence': vosSequence,  # Set the vosSequence in the view
            'title': backport.text(R.strings.ranked_battles.awards.congratulation()),  # Set the title
            'nextButtonLabel': backport.text(R.strings.ranked_battles.awards.yes())  # Set the label for the next button
        })

    def _dispose(self):
        # Override the _dispose method to clean up resources
