# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/comp7/gui/feature/comp7_modifiers_data_provider.py

# Importing required modules
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider
from comp7.constants import COMP7_SEASON_MODIFIERS_DOMAIN

# Inheriting from the ModifiersDataProvider class
class Comp7ModifiersDataProvider(ModifiersDataProvider):

    # Overriding the _readClientDomain method
    def _readClientDomain(self, modifier):
        # Returning the COMP7_SEASON_MODIFIERS_DOMAIN for the given modifier
        return COMP7_SEASON_MODIFIERS_DOMAIN
