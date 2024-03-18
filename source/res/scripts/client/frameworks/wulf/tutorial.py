# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/wulf/tutorial.py

import logging
import typing
from .py_object_binder import PyObjectEntity

# Check if the code is being type-checked
if typing.TYPE_CHECKING:
    # If so, import ViewModel from frameworks.wulf
    from frameworks.wulf import ViewModel

# Initialize the logger for this module
_logger = logging.getLogger(__name__)

# Define the Tutorial class that inherits from PyObjectEntity
class Tutorial(PyObjectEntity):
    # Define class-level attribute: a tuple of strings that lists the names of instance-level attributes
    __slots__ = ()

    # Define a class method for creating a Tutorial object
    @classmethod
    def create(cls, proxy, model):
        # Create a Tutorial object and bind it to the given proxy
        manager = Tutorial()
        manager.bind(proxy)

        # Set the model of the proxy to the given model's proxy
        proxy.setModel(model.proxy)

        # Return the created Tutorial object
        return manager

    # Define a method for getting the model of the Tutorial object
    def getModel(self):
        # Return the model of the proxy
        return self.proxy.getModel()

    # Define a method for destroying the Tutorial object
    def destroy(self):
        # Check if the proxy is not None
        if self.proxy is not None:
            # If it's not, clear the proxy
            self.proxy.clear()

        # Unbind the Tutorial object
        self.unbind()

