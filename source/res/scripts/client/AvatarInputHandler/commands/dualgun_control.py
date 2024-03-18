# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/commands/dualgun_control.py

import logging
import BigWorld
import CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from constants import DUAL_GUN, DUALGUN_CHARGER_ACTION_TYPE, DUALGUN_CHARGER_STATUS
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from helpers.CallbackDelayer import CallbackDelayer

# Define a class for shot states
class ShotStates(object):
    PREPARING = 0  # The gun is preparing to shoot
    DISABLED = 1  # The gun is disabled


# Define a class for shot controller
class ShotController(CallbackDelayer):
    # Define a property for shot locking
    isLocked = property(lambda self: self.__shotUnavailable)

    def __init__(self, threshold=__SINGLE_SHOT_THRESHOLD_DEFAULT, preChargeIndication=__PRE_CHARGE_INDICATION_DEFAULT, chargeCancelTime=__CHARGE_CANCEL_TIME_DEFAULT):
        # Initialize the superclass
        super(ShotController, self).__init__()
        # Initialize the state
        self.__state = ShotStates.DISABLED
        # Initialize the single shot threshold
        self.__singleShotThreshold = threshold
        # Initialize the pre-charge indication delay
        self.__preChargeIndicationDelay = preChargeIndication
        # Initialize the charge cancel time
        self.__chargeCancelTime = chargeCancelTime
        # Initialize the shot unavailability flag
        self.__shotUnavailable = False

    def updateState(self, state, value):
        """
        Update the state of the shot controller
        :param state: The state of the charger
        :param value: The value associated with the state
        """
        if state == DUALGUN_CHARGER_STATUS.CANCELED:
            cancelTime = value[0] if value else 0.0
            if cancelTime > 0.0:
                self.__shotUnavailable = True
                self.stopCallback(self.__setShootAvailable)
                self.delayCallback(cancelTime, self.__setShootAvailable)
            else:
                self.__setShootAvailable()
        elif state == DUALGUN_CHARGER_STATUS.APPLIED:
            self.clearCallbacks()
            self.__setShootAvailable()

    def shootKeyEvent(self, actionType):
        """
        Handle the key event for shooting
        :param actionType: The type of action
        """
        if actionType == DUALGUN_CHARGER_ACTION_TYPE.CANCEL:
            wasInCharging = self.__state == ShotStates.DISABLED
        else:
            wasInCharging = False
        BigWorld.player().shootDualGun(actionType, wasInCharging)
        if actionType == DUALGUN_CHARGER_ACTION_TYPE.START_IMMEDIATELY:
            gui_event_dispatcher.chargeReleased(keyDown=True)
        elif actionType == DUALGUN_CHARGER_ACTION_TYPE.START_WITH_DELAY:
            if self.__state == ShotStates.DISABLED:
                self.delayCallback(self.__singleShotThreshold, self.__disable)
                self.__state = ShotStates.PREPARING
            preChargeStartTime = self.__singleShotThreshold - self.__preChargeIndicationDelay
            if preChargeStartTime > 0:
                self.delayCallback(preChargeStartTime, gui_event_dispatcher.dualGunPreCharge)
            else:
                _logger.error('Incorrect pre-charge delay configuration %d', self.__preChargeIndicationDelay)
        elif actionType == DUALGUN_CHARGER_ACTION_TYPE.CANCEL:
            if self.__state == ShotStates.PREPARING:
                self.__applyShoot()
                self.__disable(direct=True)
                if self.__shotUnavailable:
                    self.__setShootAvailable()
            else:
                self.__shotUnavailable = True
                self.delayCallback(self.__chargeCancelTime, self.__setShootAvailable)
            gui_event_dispatcher.chargeReleased(keyDown=False)

    def __applyShoot(self):
        """
        Apply the shoot
        """
        if not self.__shotUnavailable:
            BigWorld.player().shoot()
        self.stopCallback(gui_event_dispatcher.dualGunPreCharge)

    def __setShootAvailable(self):
        """
        Set the shoot as available
        """
        self.__shotUnavailable = False

    def __disable(self, direct=False):
        """
        Disable the shot
        :param direct: Whether to disable directly
        """
        self.stopCallback(self.__disable)
        self.__state = ShotStates.DISABLED
        if not direct:
            gui_event_dispatcher.chargeReleased(keyDown=True)


# Define a class for dual gun controller
class DualGunController(InputHandlerCommand):
    # Define a property for shot locking
    isShotLocked = property(lambda self: self.__shotControl.isLocked)

    def __init__(self, typeDescr):
        # Initialize the active gun
        self.__activeGun = DUAL_GUN.ACTIVE_GUN.LEFT
        # Initialize the shot control
        dualGunParams = typeDescr.gun.dualGun
        if dualGunParams is not None:
            self.__shotControl = ShotController(dualGunParams.chargeThreshold, dualGunParams.preChargeIndication, dualGunParams.chargeCancelTime)
        else:
            self.__shotControl = ShotController()

    def updateChargeState(self, state, value):
        """
        Update the charge state
        :param state: The state of the charger
        :param value: The value associated with the state

