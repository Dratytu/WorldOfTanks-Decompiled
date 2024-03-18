# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/state_machine/visitor.py

from .transitions import BaseTransition  # Importing BaseTransition class from transitions module
from .exceptions import NodeError  # Importing NodeError exception from exceptions module
from .node import Node  # Importing Node class from node module

def getAncestors(node, upper=None):
    """
    Returns a list of all ancestors of the given node, up to but not including the upper node.
    
    :param node: The node to find the ancestors of.
    :type node: Node
    :param upper: The upper limit of the search, defaults to None.
    :type upper: Node, optional
    :return: A list of Node objects representing the ancestors of the given node.
    :rtype: list
    """
    if not isinstance(node, Node):
        raise NodeError('Invalid argument "node" = {}'.format(node))
    if upper is not None and not isinstance(upper, Node):
        raise NodeError('Invalid argument "upper" = {}'.format(upper))
    result = []
    found = node.getParent()
    while found != upper and found is not None:
        result.append(found)
        found = found.getParent()
    return result


def isDescendantOf(node, ancestor):
    """
    Checks if the given node is a descendant of the given ancestor node.
    
    :param node: The node to check for descendancy.
    :type node: Node
    :param ancestor: The ancestor node to check against.
    :type ancestor: Node
    :return: True if the node is a descendant of the ancestor, False otherwise.
    :rtype: bool
    """
    if not isinstance(node, Node):
        raise NodeError('Invalid argument "node" = {}'.format(node))
    if not isinstance(ancestor, Node):
        raise NodeError('Invalid argument "ancestor" = {}'.format(ancestor))
    found = node.getParent()
    while found is not None:
        if found == ancestor:
            return True
        found = found.getParent()
    return False


def getDescendantIndex(node, ancestor, filter_=None):
    """
    Returns the index of the given node in the list of children of the given ancestor node.
    
    :param node: The node to find the index of.
    :type node: Node
    :param ancestor: The ancestor node to find the children of.
    :type ancestor: Node
    :param filter_: A filter function to apply to the children of the ancestor node, defaults to None.
    :type filter_: function, optional
    :return: The index of the given node in the list of children of the given ancestor node.
    :rtype: int
    """
    children = ancestor.getChildren(filter_=filter_)
    for index, child in enumerate(children):
        if child == node or isDescendantOf(node, child):
            return index


def getLCA(nodes, upper=None):
    """
    Returns the lowest common ancestor of the given nodes.
    
    :param nodes: A list of nodes to find the lowest common ancestor of.
    :type nodes: list
    :param upper: The upper limit of the search, defaults to None.
    :type upper: Node, optional
    :return: The lowest common ancestor of the given nodes, or None if there is no such ancestor.
    :rtype: Node or None
    """
    if not nodes:
        return None
    else:
        ancestors = getAncestors(nodes[0], upper=upper)
        others = nodes[1:]
        others.reverse()
        while ancestors:
            ancestor = ancestors.pop(0)
            found = False
            for state in others:
                if isDescendantOf(state, ancestor):
                    found = True

            if found:
                return ancestor

        return None


def getEffectiveTargetStates(transition, history):
    """
    Returns
