# This module defines the different states that a battle in the bootcamp
# mode of a game can be in.

class STATE(object):
    # The initial state of the battle, before it has started.
    INITIAL = 0

    # The state where the battle is being prepared, such as loading
    # the map and setting up the teams.
    BATTLE_PREPARING = 1

    # The state where the battle is in progress.
    IN_BATTLE = 2

    # The state where the result screen is being shown, displaying
    # the outcome of the battle.
    RESULT_SCREEN = 3

    # The state where the player is back in the garage, able to select
    # a new vehicle or exit the bootcamp mode.
    IN_GARAGE = 4

    # The state where the outro video is being played, after the battle
    # has ended.
    OUTRO_VIDEO = 5

    # The state where the battle is finishing up, such as cleaning up
    # any remaining resources or data.
    FINISHING = 6
