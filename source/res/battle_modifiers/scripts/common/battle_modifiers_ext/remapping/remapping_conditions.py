# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/remapping/remapping_conditions.py

# The IRemappingCondition interface defines the methods that a remapping condition must implement
class IRemappingCondition(object):
    __slots__ = ()

    # The getName class method returns the name of the remapping condition
    @classmethod
    def getName(cls):
        raise NotImplementedError

    # The __call__ method takes a context object and returns the remapped value if the condition is met, otherwise None
    def __call__(self, ctx):
        raise NotImplementedError

# The _BaseCondition class is the base class for all remapping conditions
class _BaseCondition(IRemappingCondition):
    __slots__ = ('_remapping',)

    # The constructor takes a remapping argument, which is a mapping of sources to targets
    def __init__(self, remapping):
        self._remapping = remapping

    # The __call__ method checks if the current parameter matches any of the sources in the remapping and returns the corresponding target if a match is found
    def __call__(self, ctx):
        currentParam = self._getParam(ctx)
        for sources, target in self._remapping.iteritems():
            if currentParam in sources:
                return target

        return None

    # The _getParam method must be implemented by subclasses to return the current parameter for the given context
    def _getParam(self, ctx):
        raise NotImplementedError

# The _CaliberCondition class inherits from _BaseCondition and returns the caliber of the gun's shell
class _CaliberCondition(_BaseCondition):
    __slots__ = ()

    # The getName class method returns the name of the remapping condition
   
