# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/EmptyEntity.py

import BigWorld

# Define a class 'EmptyEntity' that inherits from 'BigWorld.Entity'
class EmptyEntity(BigWorld.Entity):

    # Constructor method for the 'EmptyEntity' class
    def __init__(self):
        # Call the constructor of the parent class 'BigWorld.Entity'
        super(EmptyEntity, self).__init__()

        # Initialize an 'AvatarFilter' object and assign it to 'self.filter'
        self.filter = BigWorld.AvatarFilter()

    # Define a method 'onLeaveWorld' for the 'EmptyEntity' class
    def onLeaveWorld(self):
        # A placeholder for any code that needs to be executed when the entity leaves the world
        pass

