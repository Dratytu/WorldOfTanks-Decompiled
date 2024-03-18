# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/markers2d/manager.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.battle.comp7.markers2d import plugins   # Import plugins for Comp7 markers
from gui.Scaleform.daapi.view.battle.shared.markers2d import manager   # Import the base MarkersManager class
from gui.Scaleform.daapi.view.battle.shared.points_of_interest import markers2d as poi_plugins   # Import PointsOfInterestPlugin

# Define Comp7MarkersManager class, which inherits from MarkersManager
class Comp7MarkersManager(MarkersManager):

    # Override the _setupPlugins method to include Comp7-specific plugins
    def _setupPlugins(self, arenaVisitor):
        # Call the parent class's method to set up basic plugins
        setup = super(Comp7MarkersManager, self)._setupPlugins(arenaVisitor)
        
        # Add Comp7-specific plugins to the setup
        setup['vehicles'] = plugins.Comp7VehicleMarkerPlugin
        setup['settings'] = plugins.Comp7SettingsPlugin
        setup['pointsOfInterest'] = poi_plugins.PointsOfInterestPlugin
        
        # Return the updated setup
        return setup
