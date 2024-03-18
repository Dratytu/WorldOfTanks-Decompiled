# This script contains the implementation for the festivity module.
# It sets up a dummy festivity factory for use in the game.

from festivity.dummy.df_factory import DummyFactory  # Importing the DummyFactory class from the festivity.dummy.df_factory module.
from skeletons.festivity_factory import IFestivityFactory  # Importing the IFestivityFactory interface from the skeletons.festivity_factory module.

# The getFestivityConfig function takes a manager object as an argument.
def getFestivityConfig(manager):
    # It creates an instance of the DummyFactory class and assigns it to the festivityFactory variable.
    festivityFactory = DummyFactory()
    
    # The addInstance method of the manager object is called with the IFestivityFactory interface and the festivityFactory instance as arguments.
    # This associates the IFestivityFactory interface with the festivityFactory instance in the manager object.
    manager.addInstance(IFestityFactory, festivityFactory)

    # The festivityFactory instance is now set up and ready to be used in the game.
