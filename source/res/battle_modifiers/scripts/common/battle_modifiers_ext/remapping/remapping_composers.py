# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/remapping/remapping_composers.py

# IComposer: An interface for remapping composers
class IComposer(object):
    __slots__ = ()

    def getValue(self, ctx, oldValue):
        """
        Returns the remapped value for the given context and old value.
        :param ctx: The context object
        :param oldValue: The old value to be remapped
        :return: The remapped value as a string
        """
        raise NotImplementedError

    def getValues(self, oldValue):
        """
        Returns a dictionary of remapped values for the given old value.
        :param oldValue: The old value to be remapped
        :return: A dictionary of remapped values
        """
        raise NotImplementedError


# _BaseComposer: An abstract base class for remapping composers
class _BaseComposer(IComposer):
    __slots__ = ('_conditions', '_targetTemplate', '_specialRules')

    def __init__(self, conditions, targetTemplate, specialRules):
        """
        Initializes the _BaseComposer class with the given conditions, target template, and special rules.
        :param conditions: A list of remapping conditions
        :param targetTemplate: The target template for remapping
        :param specialRules: A dictionary of special rules for remapping
        """
        self._conditions = conditions
        self._targetTemplate = targetTemplate
        self._specialRules = specialRules

    def getValue(self, ctx, oldValue):
        """
        Returns the remapped value for the given context and old value.
        :param ctx: The context object
        :param oldValue: The old value to be remapped
        :return: The remapped value as a string
        """
        resStr = self.__applySpecialRules(ctx, oldValue)
        if resStr is not None:
            return resStr
        else:
            resStr = self._targetTemplate
            for condition in self._conditions:
                part = condition(ctx)
                if part is None:
                    continue
                resStr = resStr.replace(''.join((_START_PATTERN, condition.getName(), _END_PATTERN)), part)

            return resStr

    def getValues(self, oldValue):
        """
        Returns a dictionary of remapped values for the given old value.
        :param oldValue: The old value to be remapped
        :return: A dictionary of remapped values
        """
        return None

    @classmethod
    def _getItemName(cls, ctx, oldValue):
        """
        Returns the item name for the given context and old value.
        :param ctx: The context object
        :param oldValue: The old value to be remapped
        :return: The item name as a string
        """
        return oldValue

    def __applySpecialRules(self, ctx, oldValue):
        """
        Applies special rules for remapping.
        :param ctx: The context object
        :param oldValue: The old value to be remapped
        :return: The remapped value as a string or None if no special rules apply
        """
        if not self._specialRules:
            return None
        else:
            itemName = self._getItemName(ctx, oldValue)
            for sources, target in self._specialRules.iteritems():
                if itemName in sources:
                    return target

            return None


# _DefaultGunEffectsComposer: A specific remapping composer for gun effects
class _DefaultGunEffectsComposer(_BaseComposer):

    @classmethod
    def _getItemName(cls, _, oldValue):
        """
        Returns the item name for the given old value in the context of gun effects.
        :param _: The context object (not used)
        :param oldValue: The old value to be remapped
        :return: The item name as a string
        """
        from items import vehicles

