# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/node.py

import weakref
from .exceptions import NodeError  # Import the custom NodeError exception

class Node(object):
    __counter = 0  # Class level counter to generate unique IDs for Node instances
    __slots__ = ('__weakref__', '__id', '__parent', '__children')  # Slots to reduce memory footprint

    def __init__(self):
        super(Node, self).__init__()
        self.__id = self.__genID()  # Generate a unique ID for the Node instance
        self.__parent = lambda: None  # Initialize the parent as None
        self.__children = []  # Initialize the children as an empty list

    def __repr__(self):
        return '{}(id={})'.format(self.__class__.__name__, self.__id)  # Represent the Node instance as a string

    def clear(self):
        self.__parent = lambda: None  # Clear the parent reference
        while self.__children:  # Clear the children references
            children = self.__children.pop()
            children.clear()

    def getNodeID(self):
        return self.__id  # Return the unique ID of the Node instance

    def getParent(self):
        return self.__parent()  # Return the parent Node instance

    def getChildren(self, filter_=None):
        return filter(filter_, self.__children)  # Return the list of children Node instances, optionally filtered

    def getChildByIndex(self, index):
        return self.__children[index] if 0 <= index < len(self.__children) else None  # Return the child Node instance at the given index

    def addChild(self, child):
        self._addChild(child)  # Add a child Node instance to this Node instance

    def removeChild(self, child):
        self._removeChild(child)  # Remove a child Node instance from this Node instance

    def visitInOrder(self, filter_=None):
        yield self  # Yield this Node instance
        for child in self.getChildren(filter_=filter_):  # Recursively yield all descendant Node instances
            for item in child.visitInOrder(filter_=filter_):
                yield item

    def _addChild(self, child):
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
        cls.__
