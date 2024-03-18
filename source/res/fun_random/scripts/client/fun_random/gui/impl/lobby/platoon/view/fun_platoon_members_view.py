# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/platoon/view/fun_platoon_members_view.py

import logging
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview

# Initialize the logger for this module
_logger = logging.getLogger(__name__)

class FunRandomMembersView(SquadMembersView, FunAssetPacksMixin, FunSubModesWatcher):
    # The prebattle type for this view
    _prebattleType = PrebattleTypes.FUNRANDOM

    @hasDesiredSubMode(defReturn='')
    def _getTitle(self):
        # Get the localized name of the sub-mode
        subModeName = backport.text(self.getDesiredSubMode().getLocalsResRoot().userName())
        # Return the localized title string with the sub-mode name
        return backport.text(R.strings.fun_random.platoonView.title(), subModeName=subModeName)

    def _setHeaderBg(self, fileName, model):
        # Set the header background image using the provided file name and the model
        model.header.setBackgroundImage(backport.image(self.getModeIconsResRoot().platoon.dyn(fileName)()))

    def _onFindPlayers(self):
        # Placeholder for the "Find Players" button click handler
        pass

    def _addSubviews(self):
        # Add the chat sub-view to the layout
        self._addSubviewToLayout(ChatSubview())

    def _addListeners(self):
        # Add view listeners
        super(FunRandomMembersView, self)._addListeners()
        self.startSubSelectionListening(self.__onSubModeSelected)

    def _removeListeners(self):
        # Remove view listeners
        self.stopSubSelectionListening(self.__onSubModeSelected)
        super(FunRandomMembersView, self)._removeListeners()

    def _updateFindPlayersButton(self, *args):
        # Update the "Find Players" button visibility (set to False)
        with self.viewModel.transaction() as model:
            model.setShouldShowFindPlayersButton(value=False)

    def __onSubModeSelected(self, *_):
        # Update the view model's raw title with the localized title string when a sub-mode is selected
        self.viewModel.setRawTitle(self._getTitle())
