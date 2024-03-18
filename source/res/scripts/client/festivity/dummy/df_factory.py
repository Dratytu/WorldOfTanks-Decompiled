# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/festivity/dummy/df_factory.py

# Import necessary classes for creating the DummyFactory
from festivity.dummy.df_controller import DummyController
from festivity.dummy.df_processor import DummyCommandsProcessor
from festivity.dummy.df_requester import DummyRequester
from skeletons.festivity_factory import IFestivityFactory

# Define the DummyFactory class that implements the IFestivityFactory interface
class DummyFactory(IFestivityFactory):

    # Initialize the DummyFactory with DummyRequester, DummyCommandsProcessor, and DummyController instances
    def __init__(self):
        self.__requester = DummyRequester()  # Create a DummyRequester instance
        self.__processor = DummyCommandsProcessor()  # Create a DummyCommandsProcessor instance
        self.__controller = DummyController()  # Create a DummyController instance

    # Implement the getRequester method from the IFestivityFactory interface
    def getRequester(self):
        return self.__requester  # Return the DummyRequester instance

    # Implement the getProcessor method from the IFestivityFactory interface
    def getProcessor(self):
        return self.__processor  # Return the DummyCommandsProcessor instance

    # Implement the getController method from the IFestivityFactory interface
    def getController(self):
        return self.__controller  # Return the DummyController instance

