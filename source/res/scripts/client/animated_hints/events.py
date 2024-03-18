# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/animated_hints/events.py

import typing  # For type checking
from gui.shared.events import HasCtxEvent  # Importing HasCtxEvent from the shared events module

# Type checking for type hinting
if typing.TYPE_CHECKING:
    from animated_hints.constants import EventAction

# Define a new class HintActionEvent that inherits from HasCtxEvent
class HintActionEvent(HasCtxEvent):
    # Define a class variable for the event type
    EVENT_TYPE = 'animated_hint_action_event'

    def __init__(self, action, ctx=None):
        # Call the constructor of the superclass with the event type and context
        super(HintActionEvent, self).__init__(eventType=self.EVENT_TYPE, ctx=ctx)

        # Store the action and context as instance variables
        self.action = action
