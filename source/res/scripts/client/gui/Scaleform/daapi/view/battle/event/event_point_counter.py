# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_point_counter.py

# Import the EventPointCounterMeta class from the gui.Scaleform.daapi.view.meta module.
# This class is the meta class for the EventPointCounter view.
from gui.Scaleform.daapi.view.meta.EventPointCounterMeta import EventPointCounterMeta

# Define the EventPointCounter class, which inherits from the EventPointCounterMeta class.
class EventPointCounter(EventPointCounterMeta):

    # Define the setPointsCount method, which takes a single argument 'count'.
    def setPointsCount(self, count):
        # Call the as_updateCountS method on 'self', passing 'count' as an argument.
        self.as_updateCountS(count)

