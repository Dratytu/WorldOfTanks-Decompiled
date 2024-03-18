# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/wulf/view/command.py

import typing
from Event import Event  # Import Event class from the Event module
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectCommand

class Command(PyObjectEntity):
    """
    A Command class that represents a command object.
    """
    __slots__ = ('__event',)

    def __init__(self):
        """
        Initialize the Command object.
        """
        super(Command, self).__init__(PyObjectCommand())
        self.__event = Event()  # Create an Event object

    def __call__(self, args=None):
        """
        Call the associated event with the given arguments.
        """
        if args is not None:
            args = (args,)
        else:
            args = ()
        self.__event(*args)
        return

    @property
    def name(self):
        """
        Get the name of the command.
        """
        return self.proxy.name

    def execute(self, args=None):
        """
        Execute the command with the given arguments.
        """
        if args is not None:
            args = (args,)
        else:
            args = ()
        self.proxy.execute(*args)
        return

    def _unbind(self):
        """
        Unbind the command from its associated event.
        """
        self.__event.clear()
        super(Command, self)._unbind()

    def _cNotify(self, args=None):
        """
        Call the associated event with the given arguments.
        """
        if args is not None:
            args = (args,)
        else:
            args = ()
        self.__event(*args)
        return

    def __iadd__(self, delegate):
        """
        Add a delegate to the associated event.
        """
        self.__event += delegate
        return self

    def __is
