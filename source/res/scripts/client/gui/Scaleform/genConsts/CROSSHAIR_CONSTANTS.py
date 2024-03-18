# This module contains constants related to the crosshair display in the game.

class CROSSHAIR_CONSTANTS(object):
    # The INVISIBLE constant represents a crosshair that is not visible on the screen.
    INVISIBLE = 0

    # The VISIBLE_NET constant represents a crosshair that is visible on the screen,
    # indicating that the player is connected to the game network.
    VISIBLE_NET = 1

    # The VISIBLE_AMMO_COUNT constant represents a crosshair that is visible on the screen
    # and displays the player's remaining ammunition count.
    VISIBLE_AMMO_COUNT = 2

    # The VISIBLE_ALL constant represents a crosshair that is visible on the screen
    # and displays all relevant information, including the player's connection status
    # and remaining ammunition count.
    VISIBLE_ALL = 3

    # The ART_SHOT_INDICATOR_NOT_ACTIVE constant represents an artillery shot indicator
    # that is not active.
    ART_SHOT_INDICATOR_NOT_ACTIVE = 0

    # The ART_SHOT_INDICATOR_ACTIVE constant represents an artillery shot indicator
    # that is active and ready for the player to fire.
    ART_SHOT_INDICATOR_ACTIVE = 1

    # The ART_SHOT_INDICATOR_EMPTY_SHELL constant represents an artillery shot indicator
    # that shows an empty shell, indicating that the player has fired their last shot.
    ART_SHOT_INDICATOR_EMPTY_SHELL = 2

    # The CROSSHAIR_BLINK_INVISIBLE constant represents a crosshair that is not visible
    # and does not blink.
    CROSSHAIR_BLINK_INVISIBLE = 0

    # The CROSSHAIR_BL
