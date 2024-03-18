# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/battle_modifier/modifier_helpers.py

from typing import Optional, Callable, Union, Dict # Importing optional, callable, union and dict types from typing module

def makeUseTypeMethods(method, copy=False):
    # This function creates a dictionary of methods for each use type in UseType.ALL
    # If method is a dictionary, it returns a copy of the method if copy is True, otherwise it returns the method itself
    # If method is not a dictionary, it returns a new dictionary with UseType.ALL as keys and method as values
    if isinstance(method, dict):
        if copy:
            return method.copy()
        return method
    return dict(((useType, method) for useType in UseType.ALL))


def createLevelTag(level):
    # This function creates a level tag in the format 'level_{level_number}'
    return 'level_' + str(level)


def parseLevelTag(levelTag):
    # This function parses a level tag and returns the level number if the tag is in the format 'level_{level_number}'
    parts = levelTag.split('_', 1)
    if not (len(parts) == 2 and parts[0] == 'level'):
        # If the tag is not in the correct format, it returns None
        return
    else:
        try:
            level = int(parts[1])
        except ValueError:
            # If the level number cannot be converted to an integer, it returns None
            level = None
        return level

