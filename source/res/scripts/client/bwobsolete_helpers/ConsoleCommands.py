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
    playerList = 'Players near you:\n'
    for i in BigWorld.entities.values():
        if i.__class__.__name__ == 'Avatar':
            playerList = playerList + i.playerName + '\n'

    FantasyDemo.addChatMsg(-1, playerList)


# help(player, string) - A console command that displays help information for other commands
def help(player, string):
    """
    A console command that displays help information for other commands.

    :param player: The invoking player object
    :param string: The name of the command to display help for, or an empty string for a list of all commands
    """
    if string:
        try:
            func = globals()[string]
            if callable(func) and func.__doc__:
                for s in func.__doc__.split('\n'):
                    FantasyDemo.addChatMsg(-1, s)

            else:
                raise 'Not callable'
        except:
            FantasyDemo.addChatMsg(-1, 'No help for ' + string)

    else:
        isCallable = lambda x: callable(globals()[x])
        ignoreList = ('getV4FromString', 'help')
        notIgnored = lambda x: x not in ignoreList
        keys = filter(isCallable, globals().keys())
        keys = filter(notIgnored, keys)
        keys.sort()
        FantasyDemo.addChatMsg(-1, '/help {command} for more info.')
        stripper = lambda c: c not in '[]\'"'
        string = filter(stripper, str(keys))
        FantasyDemo.addChatMsg(-1, string)


# target(player, string) - A console command that sends a private message to the targeted entity
def target(player, string):
    """
    A console command that sends a private message to the targeted entity.

    :param player: The invoking player object
    :param string: The message to send to the targeted entity
    """
    t = BigWorld.target()
    if t:
        try:
            t.cell.directedChat(player.id, string)
            FantasyDemo.addChatMsg(player.id, '[To ' + t.playerName + '] ' + string)
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
    if BigWorld.target() != None:
        player.physics.chase(BigWorld.target(), 2.0, 0.5)
        player.physics.velocity = (0, 0, 6.0)
    return


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
def getV4FromString(string):
    """
    A helper function that converts a string into a Math.Vector4 object.

    :param string: The string representation of the vector

