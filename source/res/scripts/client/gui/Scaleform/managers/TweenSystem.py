# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/managers/TweenSystem.py
import time
import math
import BigWorld
import Math
import resource_helper
import ResMgr
from debug_utils import LOG_ERROR
from gui.Scaleform.framework.entities.abstract.TweenManagerMeta import TweenManagerMeta

TWEEN_CONSTRAINTS_FILE_PATH = 'gui/tween_constraints.xml'
ERROR_NOT_SUCH_FILE = 'Not such file '
REQUIRED_PARAMETERS = ['moveDuration',
 'fadeDuration',
 'shadowDuration',
 'blinkingDuration',
 'translationLength',
 'fadeAlphaMax',
 'fadeAlphaMin',
 'halfTurnDuration',
 'halfTurnDelay']

class TweenManager(TweenManagerMeta):
    THRESHOLD_VALUE_IN_CURRENT_FRAME = 15

    def __init__(self):
        super(TweenManager, self).__init__()
        self.__settings = {}
        self.__id = 0
        self.__animCallback = None
        self.__lastUpdateTime = None
        self.__tweens = []
        self.__playStack = []
        self.__callBackTime = 0.02
        self.__lastStartTime = 0
        self.__loadTweenConstraintsXML()
        return

    def _populate(self):
        super(TweenManager, self)._populate()
        self.as_setDataFromXmlS(self.__settings)

    def __loadTweenConstraintsXML(self):
        if ResMgr.isFile(TWEEN_CONSTRAINTS_FILE_PATH):
            ctx, section = resource_helper.getRoot(TWEEN_CONSTRAINTS_FILE_PATH)
            settings = {}
            for ctx, subSection in resource_helper.getIterator(ctx, section):
                item = resource_helper.readItem(ctx, subSection, name='setting')
                settings[item.name] = item.value

            self.__settings.update(settings)
            self.__checkRequiredValues(self.__settings)
        else:
            LOG_ERROR(ERROR_NOT_SUCH_FILE, TWEEN_CONSTRAINTS_FILE_PATH)

    def __checkRequiredValues(self, settings):
        for key in REQUIRED_PARAMETERS:
            if key not in settings:
                LOG_ERROR('In the ' + TWEEN_CONSTRAINTS_FILE_PATH + ' there is no required parameter ' + key)

    def __onTweenStarted(self, tween):
        if not self.isTweenInStack(tween):
            tweenData = tween.getDataForAnim()
            if tweenData[3][_AbstractTween.ALPHA] != 0:
                self.__playStack.insert(0, tweenData)
            else:
                self.__playStack.append(tweenData)
        if self.__animCallback is None:
            self.__animCallback = BigWorld.callback(self.__callBackTime, self.__updatePosition)
            self.__lastUpdateTime = time.time() * 1000
        if int(time.time() * 1000) - self.__lastStartTime <= TweenManager.THRESHOLD_VALUE_IN_CURRENT_FRAME:
            self.__lastUpdateTime = time.time() * 1000
        self.__lastStartTime = int(time.time() * 1000)
        return

    def isTweenInStack(self, tween):
        tweenIdx = tween.getTweenIdx()
        countTweens = len(self.__playStack)
        for index in range(countTweens):
            tweenData = self.__playStack[index]
            curTweenIdx = tweenData[6]
            if curTweenIdx == tweenIdx:
                return True

        return False

    def __clearPlayStackElement(self, element):
        index = len(element)
        while index > 0:
            element.pop()
            index -= 1

    def _dispose(self):
        if self.__animCallback is not None:
            BigWorld.cancelCallback(self.__animCallback)
            self.__animCallback = None
        self.disposeAll()
        self.__tweens = None
        self.__playStack = None
        self.__propsInUse = None
        super(TweenManager, self)._dispose()
        return

    def createTween(self, tween):
        tweenPY = _PythonTween(self.__id)
        self.__id += 1
        tweenPY.onTweenStart += self.__onTweenStarted
        tweenPY.setFlashObject(tween)
        self.__tweens.append(tweenPY)

    def pauseAllTween(self):
        for t
