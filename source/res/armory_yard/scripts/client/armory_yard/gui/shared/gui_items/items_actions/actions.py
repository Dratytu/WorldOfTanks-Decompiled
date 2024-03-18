# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/shared/gui_items/items_actions/actions.py

from adisp import adisp_process, adisp_async # Importing adisp_process and adisp_async for asynchronous processing
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_reward_state import ArmoryYardRewardState # Importing ArmoryYardRewardState view model
from armory_yard.gui.window_events import showArmoryYardRewardWindow # Importing showArmoryYardRewardWindow function
from gui.shared.gui_items.items_actions.actions import AsyncGUIItemAction # Inheriting from AsyncGUIItemAction
from armory_yard.gui.shared.gui_items.processors.armory_yard import CollectRewardsProcessor, BuyStepTokens # Importing CollectRewardsProcessor and BuyStepTokens processors
from gui.shared.utils import decorators # Importing decorators

class CollectRewardsAction(AsyncGUIItemAction):

    def __init__(self, stageCount, closeCallback=None):
        super(CollectRewardsAction, self).__init__() # Initializing the superclass
        self.skipConfirm = True # Skipping the confirmation dialog
        self.__stageCount = stageCount # Setting the stage count
        self.__closeCallback = closeCallback # Setting the close callback

    @adisp_async # Decorator for asynchronous processing
    @adisp_process # Decorator for adisp processing
    def _action(self, callback):
        result = yield CollectRewardsProcessor().request() # Requesting the CollectRewardsProcessor
        if result.success and result.auxData is not None:
            showArmoryYardRewardWindow(bonuses=result.auxData, state=ArmoryYardRewardState.STAGE, stage=self.__stageCount, closeCallback=self.__closeCallback) # Showing the Armory Yard reward window
        callback(result) # Calling the callback function
        return


class BuyStepTokensAction(AsyncGUIItemAction):
    __slots__ = ('__count',) # Declaring a slot for the count attribute

    def __init__(self, count):
        super(BuyStepTokensAction, self).__init__() # Initializing the superclass
        self.skipConfirm = True # Skipping the confirmation dialog
        self.__count = count # Setting the count

    @adisp_async # Decorator for asynchronous processing
    @decorators.adisp_process('buyItem') # Decorator for adisp processing with 'buyItem' as the process name
    def _action(self, callback):
        result = yield BuyStepTokens(self
