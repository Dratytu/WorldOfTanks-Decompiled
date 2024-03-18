# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/states.py

from collections import namedtuple
from . import visitor
from .exceptions import StateError
from .node import Node
from .transitions import BaseTransition

# Enum for different state flags
class StateFlags(object):
    UNDEFINED = 0
    INITIAL = 1
    FINAL = 2
    HISTORY = 4
    EFFECT_TYPE_MASK = 7
    SHALLOW_HISTORY = HISTORY | 8
    DEEP_HISTORY = HISTORY | 16
    HISTORY_TYPE_MASK = 28
    SINGULAR = 32
    PARALLEL = 64

# Function to filter nodes based on their type
def _filterState(child):
    return isinstance(child, State)

# Function to filter initial states
def _filterInitialState(child):
    return _filterState(child) and child.isInitial()

# Function to filter history states
def _filterHistoryState(child):
    return _filterState(child) and child.isHistory()

# Function to filter base transitions
def _filterBaseTransition(child):
    return isinstance(child, BaseTransition)

# Class representing a state in the state machine
class State(Node):
    # Initializer for the State class
    def __init__(self, stateID='', flags=StateFlags.UNDEFINED):
        super(State, self).__init__()
        self.__stateID = stateID
        self.__flags = flags
        self.__isEntered = False

    # Properties for the state
    def getStateID(self):
        return self.__stateID

    def getFlags(self):
        return self.__flags

    # Methods for the state
    def isInitial(self):
        return self.__flags & StateFlags.INITIAL > 0

    def isSingular(self):
        return self.__flags & StateFlags.SINGULAR > 0

    def isParallel(self):
        return self.__flags & StateFlags.PARALLEL > 0

    def isFinal(self):
        return self.__flags & StateFlags.FINAL > 0

    def isHistory(self):
        return self.__flags & StateFlags.HISTORY > 0

    def isCompound(self):
        return not self.isFinal() and not self.isParallel() and self.getChildrenStates()

    def isAtomic(self):
        return self.isFinal() or not self.isFinal() and not self.getChildrenStates()

    @staticmethod
    def isMachine():
        return False

    def getMachine(self):
        found = self
        while found is not None:
            if found.isMachine():
                return found
            found = found.getParent()

        return

    def getInitial(self):
        children = self.getChildren(filter_=_filterInitialState)
        if not children:
            return None
        else:
            if len(children) > 1:
                raise StateError('State {} should be have one initial state, found {}'.format(self, children))
            return children[0]

    def addChildState(self, state):
        if not isinstance(state, State):
            raise StateError('Instance of State class is required')
        if self.isFinal():
            raise StateError('Sub-state can not be added to final state')
        self._addChild(state)

    def removeChildState(self, state):
        if not isinstance(state, State):
            raise StateError('Instance of State class is required')
        if self.isFinal():
            raise StateError('Sub-state can not be removed from final state')
        self._removeChild(state)

    def getChildrenStates(self):
        return self.getChildren(filter_=_filterState)

    def getHistoryStates(self):
        return self.getChildren(filter_=_filterHistoryState)

    def addTransition(self, transition, target=None):
        if not isinstance(transition, BaseTransition):
            raise StateError('Instance of BaseTransition class is required')
        if target is not None:
            transition.setTarget(target)
        self._addChild(transition)
        return

    def removeTransition(self, transition):
        if not isinstance(transition, BaseTransition):
            raise StateError('Instance of BaseTransition class is required')
        self._removeChild(transition)

    def getTransitions(self):
        return self.getChildren(filter_=_filterBaseTransition)

    def configure(self, *args, **kwargs):
        pass

    def enter(self):
        if self.__
