# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/node.py

import weakref
from .exceptions import NodeError  # Import the custom NodeError exception

class Node(object):
    """
    A base class representing a node in a state machine.
    """
    __counter = 0  # Class level counter to generate unique IDs for Node instances
    __slots__ = ('__weakref__', '__id', '__parent', '__children')  # Slots to reduce memory footprint

    def __init__(self):
        """
        Initialize a new Node instance.
        """
        super(Node, self).__init__()
        self.__id = self.__genID()  # Generate a unique ID for the Node instance
        self.__parent = lambda: None  # Initialize the parent as None
        self.__children = []  # Initialize the children as an empty list

    def __repr__(self):
        """
        Represent the Node instance as a string.
        """
        return '{}(id={})'.format(self.__class__.__name__, self.__id)

    def clear(self):
        """
        Clear the parent and children references of the Node instance.
        """
        self.__parent = lambda: None  # Clear the parent reference
        while self.__children:  # Clear the children references
            children = self.__children.pop()
            children.clear()

    def getNodeID(self):
        """
        Return the unique ID of the Node instance.
        """
        return self.__id

    def getParent(self):
        """
        Return the parent Node instance.
        """
        return self.__parent()

    def getChildren(self, filter_=None):
        """
        Return the list of children Node instances, optionally filtered.
        """
        return filter(filter_, self.__children)

    def getChildByIndex(self, index):
        """
        Return the child Node instance at the given index.
        """
        return self.__children[index] if 0 <= index < len(self.__children) else None

    def addChild(self, child):
        """
        Add a child Node instance to this Node instance.
        """
        self._addChild(child)

    def removeChild(self, child):
        """
        Remove a child Node instance from this Node instance.
        """
        self._removeChild(child)

    def visitInOrder(self, filter_=None):
        """
        Yield this Node instance and all descendant Node instances in order.
        """
        yield self
        for child in self.getChildren(filter_=filter_):
            for item in child.visitInOrder(filter_=filter_):
                yield item

    def _addChild(self, child):
        """
        Add a child Node instance to this Node instance.
        """
        if child is None:
            raise NodeError('Child is not defined')  # Raise a custom exception if the child is None
        if not isinstance(child, Node):
            raise NodeError('Child must extend Node class')  # Raise a custom exception if the child is not a Node instance
        if child.getParent() is not None:
            raise NodeError('Parent is already added')  # Raise a custom exception if the child already has a parent
        child.__parent = weakref.ref(self)  # Set the parent reference of the child Node instance
        if child not in self.__children:
            self.__children.append(child)  # Add the child Node instance to the list of children
        return

    def _removeChild(self, child):
        """
        Remove a child Node instance from this Node instance.
        """
        if child is None:
            raise NodeError('Child is not defined')  # Raise a custom exception if the child is None
        if not isinstance(child, Node):
            raise NodeError('Child must extend Node class')  # Raise a custom exception if the child is not a Node instance
        if child in self.__children:
            self.__children.remove(child)  # Remove the child Node instance from the list of children
            child.clear()  # Clear the child Node instance
        return

    @classmethod
    def __genID(cls):
        """
        Generate a unique ID for a Node instance.
        """
        cls.__counter += 1
        return cls.__counter

