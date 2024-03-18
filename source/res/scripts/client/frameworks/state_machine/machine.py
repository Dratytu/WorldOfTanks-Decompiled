# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/machine.py

import logging
import operator
from . import states as _states
from . import validator
from . import visitor
from .events import StateEvent
from .exceptions import StateMachineError
from .observers import BaseStateObserver
from .observers import StateObserversContainer
from .transitions import BaseTransition

_logger = logging.getLogger(__name__)

class StateMachine(_states.State):
    """
    A state machine that manages states and transitions between them.
    """
    __slots__ = ('__isRunning', '__entered', '__history', '__observers')

    def __init__(self, stateID=''):
        """
        Initialize the state machine with an initial state ID.
        """
        super(StateMachine, self).__init__(stateID=stateID)
        self.__isRunning = False
        self.__entered = []
        self.__history = {}
        self.__observers = StateObserversContainer()

    @staticmethod
    def isMachine():
        """
        Return True if the object is a state machine.
        """
        return True

    def start(self, doValidate=True):
        """
        Start the state machine, optionally validating the state machine first.
        """
        if doValidate:
            validator.validate(self)
        if self.__isRunning:
            _logger.debug('%r: Machine is already started', self)
            return
        else:
            self.__isRunning = True
            transition = _InitialTransition(target=self.getInitial())
            _logger.debug('%r: Machine is started by %r', self, transition)
            entered = self.__enter((transition,))
            transition.clear()
            self.__notify(entered, True, None)
            self.__tick()
            return

    def stop(self):
        """
        Stop the state machine.
        """
        if not self.__isRunning:
            _logger.debug('%r: Machine is not started', self)
            return
        self.__isRunning = False
        self.__observers.clear()
        self.__history.clear()
        del self.__entered[:]
        self.clear()
        _logger.debug('%r: Machine is stopped', self)

    def isStateEntered(self, stateID):
        """
        Check if a state has been entered.
        """
        for state in self.__entered:
            if state.getStateID() == stateID:
                return True

        return False

    def isRunning(self):
        """
        Check if the state machine is running.
        """
        return self.__isRunning

    def addState(self, state):
        """
        Add a state to the state machine.
        """
        self.addChildState(state)

    def removeState(self, state):
        """
        Remove a state from the state machine.
        """
        self.removeChildState(state)

    def post(self, event):
        """
        Post an event to the state machine.
        """
        _logger.debug('%r: %r is posted', self, event)
        if not isinstance(event, StateEvent):
            raise StateMachineError('Instance of StateEvent class is required')
        if not self.__isRunning:
            raise StateMachineError('State machine is not running')
        self.__tick(event=event)

    def connect(self, observer):
        """
        Connect an observer to the state machine.
        """
        self.__observers.addObserver(observer)
        for state in self.__entered:
            observer.onStateChanged(state.getStateID(), True)

    def disconnect(self, observer):
        """
        Disconnect an observer from the state machine.
        """
        self.__observers.removeObserver(observer)

    def __tick(self, event=None):
        """
        Process events and transitions.
        """
        transitions = self.__select(event)
        if transitions:
            self.__process(transitions, event)

    def __process(self, transitions, event):
        """
        Process transitions and states.
        """
        _logger.debug('%r: Start process, enabled transitions = %r', self, transitions)
        _logger.debug('%r: Snapshot before exiting states = %r', self, self.__entered)
        exited = self.__exit(transitions)
        _logger.debug('%r: Snapshot after exiting states = %r', self, self.__entered)
        entered = self.__enter(transitions)
        self.__notify(exited, False, event)
        self.__notify(entered, True, event)
        for state in self.__entered:
            if state.isFinal() and state.getParent() == self:
                self.stop()
                break

        _logger.debug('%r: Snapshot after entering states = %r', self, self.__entered)
        _logger.debug('%r: Stop process', self)

    def __select(self, event):
        """
        Select transitions based on the event.
        """
        result = []
        filtered = [ state for state in self.__entered if state.isAtomic() ]
        for state in filtered:
            states = visitor.getAncestors(state, upper=self.getParent())
            states.insert(0, state)
            transition = self.__execute(states, event)
            if transition is not None and transition not in result:
                result.append(transition)

        return result

    def __execute(self, states, event):
        """
        Execute transitions based on the event.
        """
        result = []
        for state in states:
            transitions = state.getTransitions()
            for transition in transitions:
                if transition.execute(event):
                    _logger.debug('%r: %r has execution result is True', self, transition)
                    result.append(transition)

            if result:
                result.sort(key=operator.methodcaller('getPriority'), reverse
