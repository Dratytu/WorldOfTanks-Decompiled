# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/context/styled_diffs_cache.py

import typing
from helpers import dependency
from items.components.c11n_constants import SeasonType
from skeletons.gui.customization import ICustomizationService

# A class that caches style differences (or "diffs") for the in-game customization feature.
class StyleDiffsCache(object):
    # Dependency injection for the ICustomizationService interface.
    __service = dependency.descriptor(ICustomizationService)

    def __init__(self):
        # Initialize an empty dictionary to store the diffs.
        self.__diffs = {}

    def fini(self):
        # Clear the diffs dictionary when the cache is destroyed.
        self.__diffs.clear()

    # Save diffs for a given style.
    def saveDiffs(self, style, diffs):
        # Create a new entry in the diffs dictionary for the given style,
        # or retrieve the existing entry if it already exists.
        storage = self.__diffs.setdefault(style.intCD, {})
        # Iterate over the season-diffs pairs in the input diffs dictionary.
        for season, diff in diffs.iteritems():
            # Store the diff for the given season in the storage dictionary.
            storage[season] = diff

    # Save a single diff for a given style and season.
    def saveDiff(self, style, season, diff):
        # Create a new entry in the diffs dictionary for the given style if it doesn't already exist.
        self.__diffs.setdefault(style.intCD, {})[season] = diff

    # Retrieve all diffs for a given style.
    def getDiffs(self, style):
        # Create a new dictionary to store the season-diff pairs for the given style.
        diffs = {season: self.getDiff(style, season) for season in SeasonType.COMMON_SEASONS}

