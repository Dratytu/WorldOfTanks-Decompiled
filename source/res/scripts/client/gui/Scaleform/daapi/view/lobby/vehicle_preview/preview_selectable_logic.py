# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/preview_selectable_logic.py

# Import necessary classes and functions
from ClientSelectableRankedObject import ClientSelectableRankedObject
from hangar_selectable_objects import HangarSelectableLogic

# Define the PreviewSelectableLogic class, which will handle selectable logic for vehicle preview
class PreviewSelectableLogic(HangarSelectableLogic):
    
    # Override the _filterEntity method to add a custom filtering condition
    def _filterEntity(self, entity):
        # Call the parent class's _filterEntity method to apply default filtering conditions
        isFiltered = super(PreviewSelectableLogic, self)._filterEntity(entity)
        
        # Add a custom filtering condition to exclude ClientSelectableRankedObject instances
        isFiltered = isFiltered and not isinstance(entity, ClientSelectableRankedObject)
        
        # Return the filtered result
        return isFiltered
