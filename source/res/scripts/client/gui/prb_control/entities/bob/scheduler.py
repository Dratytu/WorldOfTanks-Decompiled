# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/prb_control/entities/bob/scheduler.py
from adisp import process
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.shared.prime_time_constants import PrimeTimeStatus
from helpers import dependency
from skeletons.gui.game_control import IBobController

class BobScheduler(BaseScheduler):
    bobController = dependency.descriptor(IBobController)

    def __init__(self, entity):
        super(BobScheduler, self).__init__(entity)
        self.__isPrimeTime = False

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    def init(self):
        status, _, _ = self.bobController.getPrimeTimeStatus()
        self.__isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        self.bobController.onPrimeTimeStatusUpdated += self.__update
        self.bobController.onUpdated += self.__updateMode
        self.__show(isInit=True)

    def fini(self):
        self.bobController.onUpdated -= self.__updateMode
        self.bobController.onPrimeTimeStatusUpdated -= self.__update

    @process
    def __doLeave(self, isExit=True):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit))

    def __updateMode(self):
        if not self.bobController.isModeActive():
            self.__doLeave()
            SystemMessages.pushMessage(backport.text(R.strings.bob.systemMessage.notAvailable()), type=SystemMessages.SM_TYPE.Warning)

    def __update(self, status):
        if not self.bobController.isAvailable():
            self.__doLeave()
            return
        isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        if isPrimeTime != self.__isPrimeTime:
            self.__isPrimeTime = isPrimeTime
            self.__show()
            g_eventDispatcher.updateUI()

    def __show(self, isInit=False):
        if not self.__isPrimeTime:
            SystemMessages.pushMessage(backport.text(R.strings.bob.systemMessage.primeTime.battlesUnavailable()), type=SystemMessages.SM_TYPE.PrimeTime)
        elif not isInit:
            SystemMessages.pushMessage(backport.text(R.strings.bob.systemMessage.primeTime.battlesAvailable()), type=SystemMessages.SM_TYPE.BobBattlesAvailable)
