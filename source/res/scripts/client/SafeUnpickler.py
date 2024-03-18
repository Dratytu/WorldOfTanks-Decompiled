# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/SafeUnpickler.py

import sys
import cPickle
import StringIO

class SafeUnpickler(object):
    # A dictionary that maps safe module names to sets of safe class names
    PICKLE_SAFE = {'__builtin__': set(['object',
                     'set',
                     'frozenset',
                     'list',
                     'tuple']),
     'datetime': set(['datetime']),
     '_BWp': set(['Array', 'FixedDict']),
     'Math': set(['Vector2', 'Vector3'])}

    @classmethod
    def find_class(cls, module, name):
        # Raises an exception if the given module is not in the safe modules set
        if module not in cls.PICKLE_SAFE:
            raise cPickle.UnpicklingError('Attempting to unpickle unsafe module %s' % module)
        # Imports the given module
        __import__(module)
        mod = sys.modules[module]
        # Gets the set of safe classes for the given module
        classesSet = cls.PICKLE_SAFE[module]
        # Raises an exception if the given class is not in the safe classes set
        if name not in classesSet or classesSet is None:
            raise cPickle.UnpicklingError('Attempting to unpickle unsafe class %s' % name)
        # Gets the class from the module
        klass = getattr(mod, name)
        # Returns the class
        return klass

    @classmethod
    def loads(cls, pickle_string):
        # Creates a new Unpickler object and initializes it with a new StringIO object
        # containing the given pickle string
        pickle_obj = cPickle.Unpickler(StringIO.StringIO(pickle_string))
        # Sets the Unpickler object's find_global method to the SafeUnpickler.
