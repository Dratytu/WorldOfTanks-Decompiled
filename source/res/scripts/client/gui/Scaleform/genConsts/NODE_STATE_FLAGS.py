# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/genConsts/NODE_STATE_FLAGS.py

# A class representing various node state flags used in the game code
class NODE_STATE_FLAGS(object):
    # The flag indicating that the node is locked and cannot be accessed
    LOCKED = 1

    # The flag indicating that the next two nodes need to be unlocked
    NEXT_2_UNLOCK = 2

    # The flag indicating that the node is unlocked and can be accessed
    UNLOCKED = 4

    # The flag indicating that the player has enough XP to unlock this node
    ENOUGH_XP = 8

    # The flag indicating that the player has enough money to unlock this node
    ENOUGH_MONEY = 16

    # The flag indicating that the node is already in the player's inventory
    IN_INVENTORY = 32

    # The flag indicating that the node was already used in a battle
    WAS_IN_BATTLE = 64

    # The flag indicating that the node is an elite node
    ELITE = 128

    # The flag indicating that the node is a premium node
    PREMIUM = 256

    # The flag indicating that the node is currently selected
    SELECTED = 512

    # The flag indicating that the node is automatically unlocked
    AUTO_UNLOCKED = 1024

    # The flag indicating that the node is already installed
    INSTALLED = 2048

    # The flag indicating that the node has an action associated with it
    ACTION = 4096

    # The flag indicating that the node can be sold
    CAN_SELL = 8192

    # The flag indicating that the vehicle associated with the node can be changed
    VEHICLE_CAN_BE_CHANGED = 16384

    # The flag indicating that the vehicle associated
