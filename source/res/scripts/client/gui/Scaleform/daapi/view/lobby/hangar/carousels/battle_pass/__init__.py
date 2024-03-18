# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/battle_pass/__init__.py

class BattlePassFilterConsts(object):
    """
    A class containing constants used for filtering battle pass data.
    """

    FILTER_KEY_COMMON = 'isCommonProgression'
    """
    A constant key for filtering battle pass data by common progression.
    """

    FILTER_KEY_SEASON = 'battlePassSeason'
    """
    A constant key for filtering battle pass data by season.
    """

    FILTERS_KEYS = [FILTER_KEY_COMMON]
    """
    A list of constant keys used for filtering battle pass data.
    Currently, only common progression is supported.
    """
