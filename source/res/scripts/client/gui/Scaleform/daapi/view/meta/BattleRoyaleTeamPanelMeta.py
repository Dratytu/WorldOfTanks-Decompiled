# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleTeamPanelMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent as BaseDAAPIComponent # Importing BaseDAAPIComponent from the gui.Scaleform.framework.entities module

class BattleRoyaleTeamPanelMeta(BaseDAAPIComponent):

    # as_setInitDataS - actionscript method, sends initialization data to the client
    def as_setInitDataS(self, title, names, clans):
        # If the DAAPI is initialized, call the corresponding method on the flashObject
        return self.flashObject.as_setInitData(title, names, clans) if self._isDAAPIInited() else None

    # as_setPlayerStateS - actionscript method, sends player state data to the client
    def as_setPlayerStateS(self, index, alive, ready, hpPercent, fragsCount, vehicleLevel, icon):
        return self.flashObject.as_setPlayerState(index, alive, ready, hpPercent, fragsCount, vehicleLevel, icon) if self._isDAAPIInited() else None

    # as_setPlayerStatusS - actionscript method, sends player status data to the client
    def as_setPlayerStatusS(self, index, alive, ready):
        return self.flashObject.as_setPlayerStatus(index, alive, ready) if self._isDAAPIInited() else None

    # as_setPlayerHPS - actionscript method, sends player HP data to the client
    def as_setPlayerHPS(self, index, percent):
        return self.flashObject.as_setPlayerHP(index, percent) if self._isDAAPIInited() else None

    # as_setPlayerFragsS - actionscript method, sends player frags data to the client
    def as_setPlayerFragsS(self, index, count):
        return self.flashObject.as_setPlayerFrags(index, count) if self._isDAAPIInited() else None

    # as_setVehicleLevelS - actionscript method, sends player vehicle level data to the client
    def as_setVehicleLevelS(self, index, level):
        return self.flashObject.as_setVehicleLevel(index, level)
