# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/reward_currency_tooltip_view_model.py

# This script defines the RewardCurrencyTooltipViewModel class, which is a subclass of ViewModel.
# ViewModel is a base class for view models, which are used to store data and expose properties and commands
# for use in the user interface.

# The RewardCurrencyTooltipViewModel class has no methods or attributes of its own,
# but it has several special methods and attributes that are common to all Python classes.
# The __slots__ attribute is a list of names for instance variables that will be defined in each instance
# of the class. This is used to save memory and improve performance by preventing the creation of a
# dictionary for each instance to store its attributes.
class RewardCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    # The __init__ method is a special method that is called when an instance of the class is created.
    # It takes two arguments: properties and commands. These arguments are used to initialize the
    # instance variables of the class.
    def __init__(self, properties=1, commands=0):
        # The super() function is used to call the __init__ method of the parent class (ViewModel).
        # This is necessary to ensure that the parent class's initialization code is executed.
        super(RewardCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)

    # The getCurrencyType method is a property getter that returns the value of the currencyType
    # instance variable. This is a read-only property, as there is no corresponding setCurrencyType
    # method.
    def getCurrencyType(self):
        return self._getString(0)

    # The setCurrencyType method is a property setter that sets the value of the currencyType
    # instance variable. It takes a single argument, value, which is the new value for the
    # instance variable.

