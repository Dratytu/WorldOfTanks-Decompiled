# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventObjectivesMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities module
from gui.Scaleform.framework.entities import BaseDAAPIComponent

# Define the EventObjectivesMeta class, which inherits from BaseDAAPIComponent
class EventObjectivesMeta(BaseDAAPIComponent):

    # Define the as_updateObjectivesS method, which takes a single argument 'txt'
    def as_updateObjectivesS(self, txt):
        # If the DAAPI is initialized, call the 'as_updateObjectives' method on the flashObject with 'txt' as an argument
        return self.flashObject.as_updateObjectives(txt) if self._isDAAPIInited() else None

    # Define the as_hideS method
    def as_hideS(self):
        # If the DAAPI is initialized, call the 'as_hide' method on the flashObject
        return self.flashObject.as_hide() if self._isDAAPIInited() else None

