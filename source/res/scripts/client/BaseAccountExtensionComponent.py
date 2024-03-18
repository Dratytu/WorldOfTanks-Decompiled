# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/BaseAccountExtensionComponent.py

# Importing necessary modules:
# BigWorld: A BigWorld module for creating server-side components.
# helpers: A module containing various helper functions.
import BigWorld
from helpers import isPlayerAccount

# Defining the BaseAccountExtensionComponent class which inherits from BigWorld.StaticScriptComponent.
class BaseAccountExtensionComponent(BigWorld.StaticScriptComponent):

    # Property decorator for account.
    # This property returns the entity attribute, which represents the account.
    @property
    def account(self):
        return self.entity

    # Property decorator for base.
    # This property returns the base attribute of the account.
    @property
    def base(self):
        return self.account.base

    # Class method for getting the instance of the component.
    # It checks if the current account is a player account and if the component's name exists in the player's components.
    @classmethod
    def instance(cls):
        playerAccount = BigWorld.player()
        # The getattr function is used to safely access the component with the name cls.__name__ in the playerAccount's components.
        # If the component doesn't exist, None is returned.
        return getattr(playerAccount, cls.__name__, None) if isPlayerAccount() and cls.__name__ in playerAccount.components else None
