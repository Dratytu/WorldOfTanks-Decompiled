# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/controllers/drr_scale_ctrl.py

import weakref
import BigWorld
import Keys
from Event import Event
from account_helpers.settings_core.settings_constants import GRAPHICS
from gui import g_repeatKeyHandlers
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from helpers import dependency
from helpers import drr_scale
from skeletons.account_helpers.settings_core import ISettingsCore

# DRRScaleController class implements IBattleController interface
class DRRScaleController(IBattleController):
    # Dependency injection of ISettingsCore
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, messages):
        super(DRRScaleController, self).__init__()
        # Weak reference to messages object
        self.__messages = weakref.proxy(messages)
        # Event triggered when DRR scale changes
        self.onDRRChanged = Event()

    def getControllerID(self):
        # Returns the ID of this battle controller
        return BATTLE_CTRL_ID.DRR_SCALE

    def startControl(self):
        # Registers the repeat key event handler
        g_repeatKeyHandlers.add(self.__handleRepeatKeyEvent)

    def stopControl(self):
        # Unregisters the repeat key event handler
        self.__messages = None
        g_repeatKeyHandlers.discard(self.__handleRepeatKeyEvent)
        return

    def handleKey(self, key, isDown):
        # Handles key events
        if (key in (Keys.KEY_MINUS, Keys.KEY_NUMPADMINUS) and BigWorld.isKeyDown(Keys.KEY_RSHIFT) and isDown and not self.settingsCore.getSetting(GRAPHICS.DRR_AUTOSCALER_ENABLED)) or \
           (key in (Keys.KEY_EQUALS, Keys.KEY_ADD) and BigWorld.isKeyDown(Keys.KEY_RSHIFT) and isDown and not self.settingsCore.getSetting(GRAPHICS.DRR_AUTOSCALER_ENABLED)):
            if key in (Keys.KEY_MINUS, Keys.KEY_NUMPADMINUS):
                result = drr_scale.stepDown()
            else:
                result = drr_scale.stepUp()

            if result is not None and self.__messages:
                # Shows a vehicle message with the new DRR scale
                self.__messages.showVehicleMessage('DRR_SCALE_STEP_DOWN' if key in (Keys.KEY_MINUS, Keys.KEY_NUMPADMINUS) else 'DRR_SCALE_STEP_UP', {'scale': drr_scale.getPercent(result)})
                self.onDRRChanged()
            return True
        else:
            return False

    def __handleRepeatKeyEvent(self, event):
        # Handles repeat key events
        self.handleKey(event.key, event.isKeyDown())
