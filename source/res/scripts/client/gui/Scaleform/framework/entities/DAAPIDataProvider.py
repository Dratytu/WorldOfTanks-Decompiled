# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/DAAPIDataProvider.py

from abc import ABCMeta, abstractmethod, abstractproperty
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule
from gui.shared.utils import sortByFields

# A base class for data providers that interact with the DAAPI.
class DAAPIDataProvider(BaseDAAPIModule):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(DAAPIDataProvider, self).__init__()
        # A lambda function used to wrap items in the collection.
        self._itemWrapper = lambda x: x

    def _dispose(self):
        super(DAAPIDataProvider, self)._dispose()
        # Clear the item wrapper.
        self.clearItemWrapper()

    # A read-only property that represents the collection of items.
    @abstractproperty
    def collection(self):
        pass

    # An abstract method that builds a list of items.
    @abstractmethod
    def buildList(self, *args):
        pass

    # An abstract method that returns an empty item.
    @abstractmethod
    def emptyItem(self):
        pass

    # Sets the item wrapper.
    def setItemWrapper(self, wrapper):
        self._itemWrapper = wrapper

    # Clears the item wrapper.
    def clearItemWrapper(self):
        self._itemWrapper = lambda x: x

    # Returns the length of the collection.
    def lengthHandler(self):
        return self.pyLength()

    # Returns an item at the specified index.
    def requestItemAtHandler(self, idx):
        return self.pyRequestItemAt(idx)

    # Returns a range of items.
    def requestItemRangeHandler(self, startIndex, endIndex):
        return self.pyRequestItemRange(startIndex, endIndex)

    # Refreshes the data provider.
    def refresh(self):
        if self.flashObject is not None:
            self.flashObject.invalidate(self.pyLength())
        return

    # Returns the length of the collection.
    def pyLength(self):
        return len(self.collection)

    # Returns an item at the specified index.
    def pyRequestItemAt(self, idx):
        # Returns the item at the specified index, wrapped with the item wrapper.
        return self._itemWrapper(self.collection[int(idx)]) if -1 < idx < self.pyLength() else None

    # Returns a range of items.
    def pyRequestItemRange(self, startIndex, endIndex):
        # Returns a range of items, wrapped with the item wrapper.
        return map(self._itemWrapper, self.collection[int(startIndex):int(endIndex) + 1])

# A class for sortable data providers that inherit from DAAPIDataProvider.
class SortableDAAPIDataProvider(DAAPIDataProvider):

    def __init__(self):
        super(SortableDAAPIDataProvider, self).__init__()
        # A tuple used to store the sorting criteria.
        self._sort = ()

    # A read-only property that represents the sorted collection.
    @property
    def sortedCollection(self):
        # Returns the sorted collection based on the sorting criteria.
        return sortByFields(self._sort, self.collection)

    # A method that sorts the collection based on the specified field and order.
    def sortOnHandler(self, fieldName, options):
        return self.pySortOn(fieldName, options)

    # A method that returns the selected index.
    def getSelectedIdxHandler(self):
        return self.pyGetSelectedIdx()

    # Overrides the pyRequestItemAt method to return the item from the sorted collection.
    def pyRequestItemAt(self, idx):
        # Returns the item at the specified index, wrapped with the item wrapper.
        return self._itemWrapper(self.sortedCollection[int(idx)]) if -1 < idx < self.pyLength() else None

    # Overrides the pyRequestItemRange method to return the range of items from the sorted collection.
    def pyRequestItemRange(self, startIndex, endIndex):
        # Returns a range of items, wrapped with the item wrapper.
        return map(self._itemWrapper, self.sortedCollection[int(startIndex):int(endIndex) + 1])

    # A method that sorts the collection based on the specified fields and order.
    def pySortOn(self, fields, order):
        # Sets the sorting criteria.
        self._sort = tuple(zip(fields, order))

    # A method that returns the selected index.
    def pyGetSelectedIdx(self):
        pass

# A class for list data providers that inherit from DAAPIDataProvider.
class ListDAAPIDataProvider(DAAPIDataProvider):

    def __init__(self):
        super(ListDAAPIDataProvider, self).__init__()
        # A tuple used to store the sorting criteria.
        self._sort = ()

    # A read-only property that represents the sorted collection.
    @property
    def sortedCollection(self):
        # Returns the sorted collection based on the sorting criteria.
        return sortByFields(self._sort, self.collection)

    # A method that sorts the collection based on the specified field and order.
    def sortOnHandler(self, fieldName, options):
        return self.pySortOn(fieldName, options)

    # A method that returns the selected index.
    def getSelectedIdxHandler(self):
        return self.pyGetSelectedIdx()

    # Overrides the pyRequestItemAt method to return the item from the sorted collection.
    def pyRequestItemAt(self, idx):
        # Returns the item at the specified index, wrapped with the item wrapper.
        return self._itemWrapper(self.sortedCollection[int(idx)]) if -1 
