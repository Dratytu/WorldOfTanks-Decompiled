# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortClanBattleRoomMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def onTimerAlert(self):
        self._printOverrideError('onTimerAlert')

    def as_updateTeamHeaderTextS(self, value):
        return self.flashObject.as_updateTeamHeaderText(value) if self._isDAAPIInited() else None

    def as_setBattleRoomDataS(self, data):
        """
        :param data: Represented by FortClanBattleRoomVO (AS)
        """
        return self.flashObject.as_setBattleRoomData(data) if self._isDAAPIInited() else None

    def as_updateReadyStatusS(self, mineValue, enemyValue):
        return self.flashObject.as_updateReadyStatus(mineValue, enemyValue) if self._isDAAPIInited() else None

    def as_setTimerDeltaS(self, data):
        """
        :param data: Represented by ClanBattleTimerVO (AS)
        """
        return self.flashObject.as_setTimerDelta(data) if self._isDAAPIInited() else None

    def as_updateDirectionsS(self, data):
        """
        :param data: Represented by ConnectedDirectionsVO (AS)
        """
        return self.flashObject.as_updateDirections(data) if self._isDAAPIInited() else None

    def as_setMineClanIconS(self, value):
        return self.flashObject.as_setMineClanIcon(value) if self._isDAAPIInited() else None

    def as_setEnemyClanIconS(self, value):
        return self.flashObject.as_setEnemyClanIcon(value) if self._isDAAPIInited() else None