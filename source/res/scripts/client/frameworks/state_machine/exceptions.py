# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/exceptions.py

# This module defines custom exception classes for use in a state machine.
# These exceptions are designed to be caught and handled in a way that is
# specific to the state machine, allowing for more robust error handling
# and debugging.

# The base class for all state machine exceptions is SoftException.
# This class is derived from the built-in Exception class and provides
# additional functionality for handling exceptions in a more user-friendly
# way.

# NodeError is raised when there is an error related to a state machine
# node. This could be due to a problem with the node's configuration,
# dependencies, or other issues.
class NodeError(SoftException):
    pass


# TransitionError is raised when there is an error related to a state
# machine transition. This could be due to a problem with the transition's
# configuration, dependencies, or other issues.
class TransitionError(SoftException):
    pass


# StateError is raised when there is an error related to a state machine
# state. This could be due to a problem with the state's configuration,
# dependencies, or other issues.
class StateError(SoftException):
    pass


# StateMachineError is raised when there is an error related to the
# state machine as a whole. This could be due to a problem with the
# machine's configuration, dependencies, or other issues.
class StateMachineError(SoftException):
    pass
