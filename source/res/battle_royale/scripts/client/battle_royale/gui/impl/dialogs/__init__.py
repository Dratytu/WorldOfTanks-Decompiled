# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/dialogs/__init__.py

from enum import Enum  # Importing Enum class from Python's standard library

# Defining a custom Enum class named CurrencyTypeExtended
class CurrencyTypeExtended(Enum):
    # Defining constants for different types of in-game currencies
    CREDITS = 'credits'  # Represents in-game credits
    GOLD = 'gold'  # Represents in-game gold
    CRYSTAL = 'crystal'  # Represents in-game crystals
    XP = 'xp'  # Represents player experience points
    FREEXP = 'freeXP'  # Represents free experience points
    BR_COIN = 'brcoin'  # Represents Battle Royale coins
