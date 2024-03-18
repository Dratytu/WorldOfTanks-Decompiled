# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSectionMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent as BaseDAAPIComponent # Importing BaseDAAPIComponent to inherit from it

class ProfileSectionMeta(BaseDAAPIComponent):

    # Decorator to print an error message if a method is overridden but not implemented
    def _printOverrideError(method_name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f'Error: {method_name} method is not implemented in {func.__qualname__}')
            return wrapper
        return decorator

    # Set the active state of the profile section
    def setActive(self, value):
        self._printOverrideError('setActive')

    # Request data for the given vehicle ID
    def requestData(self, vehicleId):
        self._printOverrideError('requestData')

    # Request dossier data of the given type
    def requestDossier(self, type):
        self._printOverrideError('requestDossier')

    # Update the profile section with the provided data
    def as_updateS(self, data):
        return self.flashObject.as_update(data) if self._isDAAPIInited() else None

    # Set initial data for the profile section
    def as_setInitDataS(self, data):
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None

    # Response dossier data for the given battles type
    def as_responseDossierS(self, battlesType, data, frameLabel, emptyScreenLabel):
        return self.flashObject.as_responseDossier(battlesType, data, frameLabel, emptyScreenLabel) if self._isDAAPIInited() else None

