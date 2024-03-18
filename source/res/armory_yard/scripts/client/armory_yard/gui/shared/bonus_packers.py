# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/shared/bonus_packers.py

import logging # Importing the logging module for logging purposes
from constants import PREMIUM_ENTITLEMENTS # Importing premium entitlement constants
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS # Importing tooltip constants
from gui.impl import backport # Importing backport utility functions
from gui.impl.gen import R # Importing R (resource container)
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_rewards_vehicle_model import ArmoryYardRewardsVehicleModel # Importing ArmoryYardRewardsVehicleModel
from armory_yard_constants import isArmoryYardBattleToken, FEATURE_NAME_BASE # Importing isArmoryYardBattleToken and FEATURE_NAME_BASE
from gui.impl.backport import createTooltipData, TooltipData # Importing createTooltipData and TooltipData
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel # Importing BonusModel
from gui.shared.gui_items.Vehicle import getNationLessName # Importing getNationLessName
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap, BaseBonusUIPacker, BonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID, TokenBonusUIPacker, SimpleBonusUIPacker, VehiclesBonusUIPacker # Importing necessary classes and constants
from items.vehicles import getVehicleClassFromVehicleType # Importing getVehicleClassFromVehicleType
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker # Importing TmanTemplateBonusPacker

_logger = logging.getLogger(__name__) # Creating a logger instance
_ARMORY_YARD_REST_ICON_NAME = 'default' # Defining a constant for the rest icon name

class ArmoryYardTokenBonusUIPacker(TokenBonusUIPacker): # Defining ArmoryYardTokenBonusUIPacker class

    @classmethod # Decorator for class methods
    def _getTokenBonusPackers(cls): # Class method to get token bonus packers
        packers = super(ArmoryYardTokenBonusUIPacker, cls)._getTokenBonusPackers() # Getting token bonus packers from the parent class
        packers[FEATURE_NAME_BASE] = cls.__packArmoryYardToken # Adding the packArmoryYardToken method to the packers dictionary
        return packers # Returning the updated packers dictionary

    @classmethod # Decorator for class methods
    def _getToolTip(cls, bonus): # Class method to get the tooltip for a bonus
        return [TooltipData(tooltip=None, isSpecial=True, specialAlias=None, specialArgs=[])] # Returning an empty tooltip data list

    @classmethod # Decorator for class methods
    def _getContentId(cls, bonus): # Class method to get the content ID for a bonus
        return [R.views.armory_yard.lobby.feature.tooltips.ArmoryYardCurrencyTooltipView()] # Returning the content ID for Armory Yard currency tooltip view

    @classmethod # Decorator for class methods
    def _getTokenBonusType(cls, tokenID, complexToken): # Class method to get the token bonus type
        if isArmoryYardBattleToken(tokenID): # If the token ID is an Armory Yard battle token
            return FEATURE_NAME_BASE # Return the FEATURE_NAME_BASE
        return '' if tokenID == 'ny24_yaga' else super(ArmoryYardTokenBonusUIPacker, cls)._getTokenBonusType(tokenID, complexToken) # Otherwise, return an empty string or the token bonus type from the parent class

    @classmethod # Decorator for class methods
    def __packArmoryYardToken(cls, model, _, *args): # Class method to pack the Armory Yard token
        model.setIconSmall(backport.image(R.images.armory_yard.gui.maps.icons.token.s20())) # Setting the small icon for the model
        model.setIconBig(backport.image(R.images.armory_yard.gui.maps.icons.token.s44())) # Setting the big icon for the model
        return model # Returning the packed model

class ArmoryYardMainVehiclesBonusUIPacker(BaseBonusUIPacker): # Defining ArmoryYardMainVehiclesBonusUIPacker class

    @classmethod # Decorator for class methods
    def _pack(cls, bonus): # Class method to pack the bonus
        return [ cls._packVehicle(vehicle, vehicleInfo) for vehicle, vehicleInfo in bonus.getVehicles() ] # Packing each vehicle and vehicle info in the bonus

    @classmethod # Decorator for class methods
    def _getToolTip(cls, bonus): # Class method to get the tooltip for a bonus
        return [ createTooltipData(isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.ARMORY_YARD_AWARD_VEHICLE, specialArgs=[vehicle.intCD]) for vehicle, _ in bonus.getVehicles() ] # Creating tooltip data for each vehicle

    @classmethod # Decorator for class methods
    def _getContentId(cls, bonus): # Class method to get the content ID for a bonus
        return [ BACKPORT_TOOLTIP_CONTENT_ID for _ in bonus.getVehicles() ] # Returning the content ID for each vehicle

    @classmethod # Decorator for class methods
    def _packVehicle(cls, vehicle, _): # Class method to pack a vehicle
        vehicleModel = ArmoryYardRewardsVehicleModel() # Creating an instance of ArmoryYardRewardsV
