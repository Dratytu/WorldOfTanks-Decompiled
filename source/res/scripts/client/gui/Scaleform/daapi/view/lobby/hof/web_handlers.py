# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hof/web_handlers.py

# Import necessary modules and classes
from web.web_client_api import webApiCollection, w2capi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.ui.browser import CloseBrowserViewWebApiMixin
from web.web_client_api.vehicles import VehiclesWebApi
from web.web_client_api.request import RequestWebApi
from web.web_client_api.sound import SoundWebApi
from web.web_client_api.ui import OpenWindowWebApi, OpenTabWebApi, ContextMenuWebApi

# Define the createHofWebHandlers function
def createHofWebHandlers():

    # Define the _CloseWindowWebApi class that inherits from CloseBrowserViewWebApiMixin
    @w2capi(name='close_window', key='window_id')
    class _CloseWindowWebApi(CloseBrowserViewWebApiMixin):
        pass

    # Return a webApiCollection instance containing various web API classes
    return webApiCollection(_CloseWindowWebApi, OpenWindowWebApi, OpenTabWebApi, RequestWebApi, SoundWebApi, ContextMenuWebApi, ShopWebApi, VehiclesWebApi)
