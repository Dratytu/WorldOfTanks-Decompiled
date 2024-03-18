# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/Listener.py

import copy
import weakref

class Listenable:
    """
    A class that can have listeners added to it.
    """

    def __init__(self):
        """
        Initialize a new Listenable instance.
        """
        self.listeners = _Listeners()

    def addListener(self, eventName, fn):
        """
        Add a listener function (fn) to the given eventName.
        """
        self.listeners.addListener(eventName, fn)

    def removeListener(self, eventName, fn):
        """
        Remove the given listener function (fn) from the given eventName.
        """
        self.listeners.removeListener(eventName, fn)


class _Listeners(object):
    """
    A class that manages a collection of listeners for different eventNames.
    """

    def __init__(self):
        """
        Initialize a new _Listeners instance.
        """
        self.listeners = {}

    def addListener(self, eventName, fn):
        """

