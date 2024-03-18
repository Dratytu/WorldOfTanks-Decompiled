# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/tooltips/level_reserves_tooltip.py

# Import necessary modules and dependencies
from frameworks.wulf import ViewFlags, ViewSettings
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.level_reserves_tooltip_model import LevelReservesTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

# Define the LevelReservesTooltip class
class LevelReservesTooltip(ViewImpl):
    # Inject the IEpicBattleMetaGameController dependency
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self):
        # Initialize the view with settings and a LevelReservesTooltipModel
        settings = ViewSettings(R.views.frontline.lobby.tooltips.LevelReservesTooltip(), ViewFlags.VIEW, LevelReservesTooltipModel())
        super(LevelReservesTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        # Return the view model
        return super(LevelReservesTooltip, self).getViewModel()

    def _on
