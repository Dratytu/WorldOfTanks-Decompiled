# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/br_coin_tooltip_view_model.py

# This file defines the `BrCoinTooltipViewModel` class, which is a subclass of `ViewModel`.
# The `BrCoinTooltipViewModel` class is used for managing view model related logic in the Battle Royale Coin Tooltip.
# It does not contain any specific business logic or data processing methods.
# The class is initialized with a given number of properties and commands, which are defined by the user.

class BrCoinTooltipViewModel(ViewModel):
    # The `BrCoinTooltipViewModel` class is initialized with two optional parameters:
    # - properties (int): The number of properties associated with the view model.
    # - commands (int): The number of commands associated with the view model.
    
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        # Calls the constructor of the superclass, initializing the object with the given properties and commands.
        super(BrCoinTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        # This method is called by the superclass constructor to perform any additional initialization.
        # In this case, it does not contain any specific logic and only calls the superclass's _initialize() method.
        super(BrCoinTooltipViewModel, self)._initialize()
