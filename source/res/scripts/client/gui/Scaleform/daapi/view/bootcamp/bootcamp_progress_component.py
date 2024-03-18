# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/bootcamp_progress_component.py

# Import necessary modules and classes
from frameworks.wulf import ViewFlags  # Import ViewFlags from wulf framework for setting view properties

from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor  # Import InjectComponentAdaptor for injecting components
from gui.prb_control.entities.listener import IGlobalListener  # Import IGlobalListener for handling global events

from gui.impl.lobby.bootcamp.bootcamp_progress_widget_view import BootcampProgressWidgetView  # Import BootcampProgressWidgetView for creating the view
from gui.Scaleform.daapi.view.meta.BootcampProgressMeta import BootcampProgressMeta  # Import BootcampProgressMeta for defining the view's meta interface

# The BootcampProgressComponent class inherits from InjectComponentAdaptor and IGlobalListener
class BootcampProgressComponent(InjectComponentAdaptor, IGlobalListener):

    # The __init__ method initializes the BootcampProgressComponent instance
    def __init__(self):
        # Call the constructor of the InjectComponentAdaptor class
        super(BootcampProgressComponent, self).__init__()
        # Set the view flags for the BootcampProgressWidgetView
        self._flags = ViewFlags.window | ViewFlags.back

    # The _populate method is used to create and configure the BootcampProgressWidgetView
    def _populate(self):
        # Create an instance of the BootcampProgressWidgetView
        self.children.append(BootcampProgressWidgetView(self._flags))

    # The onGlobalListenerEvent method is called when a global event occurs
    def onGlobalListenerEvent(self, event_name, event_data):
        # If the event name is 'onBootcampProgressUpdated', update the BootcampProgressWidgetView
        if event_name == 'onBootcampProgressUpdated':
            self.getView().update(event
