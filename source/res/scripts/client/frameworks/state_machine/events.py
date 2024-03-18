# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/events.py

class StateEvent(object):
    # A class representing a state event in a state machine.
    # It holds a dictionary of arguments passed to the event.
    __slots__ = ('__arguments',)

    def __init__(self, *args, **kwargs):
        # Initialize the StateEvent object.
        # The arguments are stored in a dictionary.
        super(StateEvent, self).__init__()
        self.__arguments = kwargs

    def __repr__(self):
        # Provide a human-readable representation of the object.
        return '{}({})'.format(self.__class__.__name__, id(self))

    def getArgument(self, name, default=None):
        # Get an argument from the dictionary by name.
        # If the argument does not exist, return the default value.
        return self.__arguments.get(name, default)


class StringEvent(StateEvent):
    # A class representing a string state event in a state machine.
    # It holds a token and a dictionary of arguments passed to the event.
    __slots__ = ('__token',)

    def __init__(self, token, **kwargs):
        # Initialize the StringEvent object.
        # The token and arguments are stored.
        super(StringEvent, self).__init__(**kwargs)
        self.__token = token

    def __repr__(self):
        # Provide a human-readable representation of the object.
        return '{}({})'.format(self.__class__.__name__, self.__token)

    @property
    def token(self):
        # Get the token of the StringEvent object.
        return self.__token
