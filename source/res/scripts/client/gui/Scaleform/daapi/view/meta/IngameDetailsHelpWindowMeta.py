# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameDetailsHelpWindowMeta.py

# Import the AbstractWindowView class from the gui.Scaleform.framework.entities.abstract.AbstractWindowView module
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

# Define the IngameDetailsHelpWindowMeta class, which inherits from AbstractWindowView
class IngameDetailsHelpWindowMeta(AbstractWindowView):

    # Define the requestPageData method, which takes an index as its argument
    def requestPageData(self, index):
        # Print an error message indicating that the requestPageData method has been overridden
        self._printOverrideError('requestPageData')

    # Define the as_setPaginatorDataS method, which takes pages as its argument
    def as_setPaginatorDataS(self, pages):
        # If the DAAPI has been initialized, return the result of calling the as_setPaginatorData method on the flashObject with pages as its argument
        return self.flashObject.as_setPaginatorData(pages) if self._isDAAPIInited() else None

    # Define the as_setPageDataS method, which takes data as its argument
    def as_setPageDataS(self, data):
        # If the DAAPI has been initialized, return the result of calling the as_setPageData method on the flashObject with data as its argument
        return self.flashObject.as_setPageData(data) if self._isDAAPIInited() else None

