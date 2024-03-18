# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/winback/full_stats.py

# Import the FullStatsComponent class from the classic battle module
from gui.Scaleform.daapi.view.battle.classic.full_stats import FullStatsComponent

# Define the WinbackFullStatsComponent class, which inherits from FullStatsComponent
class WinbackFullStatsComponent(FullStatsComponent):

    # This class has a single static method

    @staticmethod
    def _buildTabs(builder):
        # This method builds and returns a list of tabs for the stats view

        # Add a 'statistics' tab to the builder
        builder.addStatisticsTab()

        # Add a 'boosters' tab to the builder
        builder.addBoostersTab()

        # Return the list of tabs created by the builder
        return builder.getTabs()

