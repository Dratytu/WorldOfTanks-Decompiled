# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/states/StateInitial.py

# Import necessary modules and classes
from bootcamp.states import STATE
from bootcamp.states.AbstractState import AbstractState

# Define the StateInitial class, which inherits from AbstractState
class StateInitial(AbstractState):

    # Initialize the class with the state type set to STATE.INITIAL
    def __init__(self):
        super(StateInitial, self).__init__(STATE.INITIAL)

    # Define a method to handle key events, which currently does nothing
    def handleKeyEvent(self, event):
        pass

    # Define a method for what to do when the state is activated, which currently does nothing
    def _doActivate(self):
        pass

    # Define a method for what to do when the state is deactivated, which currently does nothing
    def _doDeactivate(self):
        pass

