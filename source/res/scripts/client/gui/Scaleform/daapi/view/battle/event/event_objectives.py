# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_objectives.py

# Import the EventObjectivesMeta class from the gui.Scaleform.daapi.view.meta package
from gui.Scaleform.daapi.view.meta import EventObjectivesMeta

# Define the EventObjectivesPanel class that inherits from EventObjectivesMeta
class EventObjectivesPanel(EventObjectivesMeta):

    # Define the updateObjectives method that takes a single argument 'txt'
    def updateObjectives(self, txt):
        # Call the as_updateObjectivesS method on 'self' and pass 'txt' as a parameter
        self.as_updateObjectivesS(txt)

    # Define the hide method
    def hide(self):
        # Call the as_hideS method on 'self'
        self.as_hideS()

