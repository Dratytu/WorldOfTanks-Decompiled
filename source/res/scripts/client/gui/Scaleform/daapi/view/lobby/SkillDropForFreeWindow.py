# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/SkillDropForFreeWindow.py

import time
from chat_shared import SYS_MESSAGE_TYPE
from constants import DROP_SKILL_OPTIONS, FREE_DROP_SKILL_TOKEN
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.SkillDropForFreeMeta import SkillDropForFreeMeta
from gui.shared.gui_items.Tankman import Tankman
from gui.shared.gui_items.processors.tankman import TankmanDropSkills
from gui.shared.gui_items.serializers import packTankman, repackTankmanWithSkinData
from gui.shared.money import Money, Currency
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.utils import decorators
from helpers import dependency, time_utils
from items import tankmen
from messenger import MessengerEntry
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

# Subclass of SkillDropForFreeMeta, responsible for displaying the Skill Drop For Free window in the Lobby.
class SkillDropForFreeWindow(SkillDropForFreeMeta):
    # Dependency injection for IItemsCache and ILobbyContext.
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.instance(ILobbyContext)

    def __init__(self, ctx=None):
        # Initialize the superclass and store the tankmanID from the context.
        super(SkillDropForFreeWindow, self).__init__()
        self.tmanInvID = ctx.get('tankmanID')

    def __setData(self, *_):
        # Retrieve the items and tankman objects from the IItemsCache instance.
        items = self.itemsCache.items
        tankman = items.getTankman(self.tmanInvID)

        # Return if the tankman object is None, indicating that the tankman is not found.
        if tankman is None:
            self.onWindowClose()
            return

        # Initialize an empty list for storing drop skills cost data.
        dropSkillsCost = []

        # Iterate through the sorted keys of drop skills cost from the IItemsCache instance.
        for k in sorted(items.shop.dropSkillsCost.keys()):
            # Retrieve the skill cost and default skill cost for the current key.
            skillCost = items.shop.dropSkillsCost[k]
            defaultSkillCots = items.shop.defaults.dropSkillsCost[k]

            # Convert the skill cost and default skill cost to Money objects.
            price = Money(**skillCost)
            defaultPrice = Money(**defaultSkillCots)

            # Initialize an action variable for storing the action tooltip data.
            action = None

            # If the skill cost and default skill cost are not equal, create the action tooltip data.
            if price != defaultPrice:
                key = '{}DropSkillsCost'.format(price.getCurrency(byWeight=True))
                action = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, key, True, price, defaultPrice)

            # Append the skill cost dictionary with the action data to the drop skills cost list.
            dropSkillsCost.append({'action': action,
                                   'xpReuseFraction': 1.0,
                                   'gold': 0,
                                   'credits': 0})

        # Append a dictionary with default values to the drop skills cost list.
        dropSkillsCost.append({'action': None,
                               'xpReuseFraction': 1.0,
                               'gold': 0,
                               'credits': 0})

        # Calculate the number of available skills for the tankman.
        skills_count = tankmen.getSkillsConfig().getNumberOfActiveSkills()
        lenSkills = len(tankman.skills)
        availableSkillsCount = skills_count - lenSkills

        # Check if the tankman has new skills to drop.
        hasNewSkills = tankman.roleLevel == tankmen.MAX_SKILL_LEVEL and availableSkillsCount and (tankman.descriptor.lastSkillLevel == tankmen.MAX_SKILL_LEVEL or not lenSkills)

        # Serialize the tankman object to a dictionary.
        tankmanData = packTankman(tankman, isCountPermanentSkills=False)

        # Repack the tankman dictionary with skin data.
        repackTankmanWithSkinData(tankman, tankmanData)

        # Retrieve the expiry time for the free drop skill token from the IItemsCache instance.
        expiryTime = self.itemsCache.items.tokens.getTokenExpiryTime(FREE_DROP_SKILL_TOKEN)

        # Call the as_setDataS method of the superclass with the processed data.
        self.as_setDataS({'tankman': tankmanData,
                          'dropSkillsCost': dropSkillsCost,
                          'hasNewSkills': hasNewSkills,
                          'newSkills': tankman.newSkillCount,
                          'blanks': 0,
                          'timeLeft': expiryTime - time_utils.getServerUTCTime()})

        return

    def _populate(self):
        # Call the _populate method of the superclass.
        super(SkillDropForFreeWindow, self)._populate()

        # Call the __setData method to initialize the window data.
        self.__setData()

        # Register a callback for the onSyncCompleted event of the IItemsCache instance.
        self.itemsCache.onSyncCompleted += self.__setData

        # Register callbacks for the inventory and wallet resource update events
