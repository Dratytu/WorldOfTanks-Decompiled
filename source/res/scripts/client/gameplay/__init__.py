# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gameplay/__init__.py

# The special list `__all__` is used to specify the public names exported by a module.
# In this case, only the `getGameplayConfig` function is exported.
__all__ = ('getGameplayConfig',)

def getGameplayConfig(manager):
    # Import the GameplayLogic class from the gameplay.delegator module.
    from gameplay.delegator import GameplayLogic
    
    # Import the `create` function from the gameplay.machine module.
    from gameplay.machine import create
    
    # Import the IGameplayLogic interface from the skeletons.gameplay module.
    from skeletons.gameplay import IGameplayLogic
    
    # Add an instance of the IGameplayLogic interface to the manager,
    # using the GameplayLogic class and the `create` function.
    # The instance will be automatically finalized and removed from the manager
    # when the 'stop' method is called.
    manager.addInstance(IGameplayLogic, GameplayLogic(create()), finalizer='stop')

