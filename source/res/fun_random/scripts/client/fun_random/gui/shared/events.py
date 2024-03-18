# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/shared/events.py

# Importing the enum module from the Python standard library, which is used for defining enumerations.
import enum

# Importing HasCtxEvent and SharedEvent from gui.shared.events, which are likely base classes or mixins for custom event classes.
from gui.shared.events import HasCtxEvent, SharedEvent

# Importing the event_bus module from gui.shared, which is likely used for managing and dispatching events in the application.
from gui.shared.event_bus import SharedEvent


# An enumeration named FunRandomEvents is defined using the enum module.
# This enumeration likely contains constants for various events in the fun_random module.
class FunRandomEvents(enum.Enum):
    pass


# A class named FunRandomEvent is defined, which likely inherits from HasCtxEvent and SharedEvent.
class FunRandomEvent(HasCtxEvent, SharedEvent):

    # The __init__ method is defined to initialize the FunRandomEvent instance.
    def __init__(self, ctx=None):
        # The super() function is used to call the __init__ method of the superclass, HasCtxEvent.
        super(FunRandomEvent, self).__init__(ctx)

