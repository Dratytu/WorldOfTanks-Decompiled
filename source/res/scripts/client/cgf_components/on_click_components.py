# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_components/on_click_components.py

# Import necessary modules and libraries
import logging
import CGF
from GenericComponents import VSEComponent
from adisp import adisp_process
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery
from constants import MarathonConfig, IS_CLIENT
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.utils import IHangarSpace

# Define a logger for this module
_logger = logging.getLogger(__name__)

# Define a dictionary for marathon video URL providers
URL_PROVIDERS = {'MARATHON_VIDEO_URL_PROVIDER': getMarathonVideoUrl}

# Define the OpenBrowserOnClickComponent class
@registerComponent
class OpenBrowserOnClickComponent(object):
    # Set the domain and urlProvider properties
    domain = CGF.DomainOption.DomainClient
    urlProvider = ComponentProperty(type=CGFMetaTypes.STRING, editorName='url provider', value='MARATHON_VIDEO_URL_PROVIDER')

    # Initialize the class
    def __init__(self):
        super(OpenBrowserOnClickComponent, self).__init__()
        # Initialize the __urlParser attribute
        self.__urlParser = URLMacros()

    # Define the doAction method
    def doAction(self):
        self.__openBrowser()

    # Define the __openBrowser method with @adisp_process decorator
    @adisp_process
    def __openBrowser(self):
        # Get the urlProvider function
        getterFunc = URL_PROVIDERS[self.urlProvider]
        # Get the unparsed URL
        unparsedUrl = getterFunc()
        # Parse the URL
        url = yield self.__urlParser.parse(unparsedUrl)
        # Show the browser overlay view with the parsed URL
        showBrowserOverlayView(url, alias=VIEW_ALIAS.BROWSER_OVERLAY)

# Define the getMarathonVideoUrl function
def getMarathonVideoUrl():
    lobbyContext = dependency.instance(ILobbyContext)
    return lobbyContext.getServerSettings().getMarathonConfig()[MarathonConfig.VIDEO_CONTENT_URL]

# Define the OpenCollectionOnClickComponent class
@registerComponent
class OpenCollectionOnClickComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'Open collections on Click'
    collectionID = ComponentProperty(type=CGFMetaTypes.INT, editorName='collection Id')

    # Define the doAction method
    def doAction(self):
        if self.collectionID:
            # Show the collection window with the specified collection ID
            backText = backport.text(R.strings.menu.viewHeader.backBtn.descrLabel.hangar())
            showCollectionWindow(self.collectionID, backBtnText=backText)

# Define the ClientSelectableComponentsManager class
@autoregister(presentInAllWorlds=False, category='lobby')
class ClientSelectableComponentsManager(CGF.ComponentManager):

    # Define the handleOpenBrowserOnClickAdded method
    @onAddedQuery(OpenBrowserOnClickComponent, SelectionComponent)
    def handleOpenBrowserOnClickAdded(self, openBrowserOnClickComponent, selectionComponent):
        # Register the onClickAction event for the SelectionComponent
        selectionComponent.onClickAction += openBrowserOnClickComponent.doAction

    # Define the handleOpenBrowserOnClickRemoved method
    @onRemovedQuery(OpenBrowserOnClickComponent, SelectionComponent)
    def handleOpenBrowserOnClickRemoved(self, openBrowserOnClickComponent, selectionComponent):
        # Unregister the onClickAction event for the SelectionComponent
        selectionComponent.onClickAction -= openBrowserOnClickComponent.doAction

    # Define the handleOpenCollectionOnClickAdded method
    @onAddedQuery(OpenCollectionOnClickComponent, SelectionComponent)
    def handleOpenCollectionOnClickAdded(self, openCollectionOnClickComponent, selectionComponent):
        # Register the onClickAction event for the SelectionComponent
        selectionComponent.onClickAction += openCollectionOnClickComponent.doAction

    # Define the handleOpenCollectionOnClickRemoved method
    @onRemovedQuery(OpenCollectionOnClickComponent, SelectionComponent)
    def handleOpenCollectionOnClickRemoved(self, openCollectionOnClickComponent, selectionComponent):
        # Unregister the onClickAction event for the SelectionComponent
        selectionComponent.onClickAction -= openCollectionOnClickComponent.doAction

# Define the ClickVSEComponentsManager class
@autoregister(presentInAllWorlds=True, category='lobby')
class ClickVSEComponentsManager(CGF.ComponentManager):

    # Define the handleComponentAdded method
    @onAddedQuery(SelectionComponent, VSEComponent)
    def handleComponentAdded(self, selectionComponent, vseComponent):
        # Register the onGameObjectClick event for the VSEComponent
        selectionComponent.onClickAction += vseComponent.context.onGameObjectClick

    # Define the handleComponentRemoved method
    @onRemovedQuery(SelectionComponent, VSEComponent)
    def handleComponentRemoved(self, selectionComponent, vseComponent):
        # Unregister the onGameObjectClick event for the VSEComponent
        selectionComponent.onClickAction -= vseComponent.context.onGameObjectClick

# Define the ClickManager class
class ClickManager(CGF.ComponentManager):
    _hangarSpace = dependency.descriptor(IHangarSpace)

    # Initialize the class
    def __init__(self, *args):
        super(ClickManager, self).__init__(*args)
        # Initialize the _selectedGO attribute
        self._selectedGO = None
        return

    # Define the activate method
    def activate(self):
        # Register the onMouseDown and onMouseUp events for the _hangarSpace
        self._hangarSpace.onMouseDown += self._onMouseDown
        self._hangarSpace.onMouseUp += self._onMouseUp

    # Define the deactivate method
    def
