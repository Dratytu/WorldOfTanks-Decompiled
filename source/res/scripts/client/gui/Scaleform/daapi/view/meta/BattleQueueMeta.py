# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleQueueMeta.py
from gui.Scaleform.framework.entities.View import View

class BattleQueueMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def startClick(self):
        self._printOverrideError('startClick')

    def exitClick(self):
        self._printOverrideError('exitClick')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def as_setTimerS(self, text):
        return self.flashObject.as_setTimer(text) if self._isDAAPIInited() else None

    def as_setTypeInfoS(self, data):
        """
        :param data: Represented by BattleQueueTypeInfoVO (AS)
        """
        return self.flashObject.as_setTypeInfo(data) if self._isDAAPIInited() else None

    def as_setPlayersS(self, text):
        return self.flashObject.as_setPlayers(text) if self._isDAAPIInited() else None

    def as_setListByTypeS(self, data):
        """
        :param data: Represented by BattleQueueListDataVO (AS)
        """
        return self.flashObject.as_setListByType(data) if self._isDAAPIInited() else None

    def as_showStartS(self, vis):
        return self.flashObject.as_showStart(vis) if self._isDAAPIInited() else None

    def as_showExitS(self, vis):
        return self.flashObject.as_showExit(vis) if self._isDAAPIInited() else None