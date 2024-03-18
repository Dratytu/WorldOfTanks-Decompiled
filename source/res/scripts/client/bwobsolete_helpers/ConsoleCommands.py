# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/ConsoleCommands.py

import BigWorld  # Import the BigWorld module for entity management and game world interaction
import FantasyDemo  # Import the FantasyDemo module for adding chat messages
import Avatar  # Import the Avatar module for player-related functionality
import Math  # Import the Math module for vector and matrix operations
import FDGUI  # Import the FDGUI module for GUI-related functionality
import re  # Import the re module for regular expression operations

# who(player, string) - A console command that lists players near the invoker
def who(player, string):
    """
    A console command that lists players near the invoker.

    :param player: The invoking player object
    :param string: Not used in this function
    """
    player_list = 'Players near you:\n'
    for entity in BigWorld.entities.values():
        if isinstance(entity, Avatar.Avatar):
            player_list += entity.playerName + '\n'

    FantasyDemo.addChatMsg(-1, player_list)


# help(player, string) - A console command that displays help information for other commands
def help(player, string):
    """
    A console command that displays help information for other commands.

    :param player: The invoking player object
    :param string: The name of the command to display help for, or an empty string for a list of all commands
    """
    if string:
        try:
            function = globals()[string]
            if callable(function) and function.__doc__:
                for line in function.__doc__.split('\n'):
                    FantasyDemo.addChatMsg(-1, line)

            else:
                raise 'Not callable'
        except:
            FantasyDemo.addChatMsg(-1, 'No help for ' + string)

    else:
        is_callable = lambda x: callable(globals()[x])
        ignore_list = ('getV4FromString', 'help')
        not_ignored = lambda x: x not in ignore_list
        keys = filter(is_callable, globals().keys())
        keys = filter(not_ignored, keys)
        keys.sort()
        FantasyDemo.addChatMsg(-1, '/help {command} for more info.'.format(command=keys[0]))
        stripper = lambda c: c not in '[]\'"'
        string = ' '.join(filter(stripper, str(keys)))
        FantasyDemo.addChatMsg(-1, string)


# target(player, string) - A console command that sends a private message to the targeted entity
def target(player, string):
    """
    A console command that sends a private message to the targeted entity.

    :param player: The invoking player object
    :param string: The message to send to the targeted entity
    """
    target_entity = BigWorld.target()
    if target_entity is not None:
        try:
            target_entity.cell.directedChat(player.id, string)
            FantasyDemo.addChatMsg(player.id, '[To {target}] {message}'.format(target=target_entity.playerName, message=string))
        except:
            pass


# pushUp(player, string) - A console command that pushes the player up
def pushUp(player, string):
    """
    A console command that pushes the player up.

    :param player: The invoking player object
    :param string: Not used in this function
    """
    player.pushUpKey()


# pullUp(player, string) - A console command that pulls the player up
def pullUp(player, string):
    """
    A console command that pulls the player up.

    :param player: The invoking player object
    :param string: Not used in this function
    """
    player.pullUpKey()


# follow(player, string) - A console command that makes the player follow the targeted entity
def follow(player, string):
    """
    A console command that makes the player follow the targeted entity.

    :param player: The invoking player object
    :param string: Not used in this function
    """
    target_entity = BigWorld.target()
    if target_entity is not None:
        player.physics.chase(target_entity, 2.0, 0.5)
        player.physics.velocity = (0, 0, 6.0)


# summon(player, string) - A console command that summons an entity by name
def summon(player, string):
    """
    A console command that summons an entity by name.

    :param player: The invoking player object
    :param string: The name of the entity to summon
    """
    if isinstance(BigWorld.connectedEntity(), Avatar.Avatar):
        BigWorld.connectedEntity().cell.summonEntity(str(string))
    else:
        FantasyDemo.addChatMsg(-1, 'Summon can only be called when connected to the server')


# weather(player, string) - A console command that sets the current weather
def weather(player, string):
    """
    A console command that sets the current weather.

    :param player: The invoking player object
    :param string: The name of the weather type
    """
    import Weather  # Import the Weather module for weather management
    Weather.weather().toggleRandomWeather(False)
    Weather.weather().summon(str(string))


# rain(player, string) - A console command that sets the rain intensity
def rain(player, string):
    """
    A console command that sets the rain intensity.

    :param player: The invoking player object
    :param string: The rain intensity as a float
    """
    import Weather  # Import the Weather module for weather management
    Weather.weather().rain(float(string))


# getV4FromString(string) - A helper function that converts a string into a Math.Vector4 object
def getV4
