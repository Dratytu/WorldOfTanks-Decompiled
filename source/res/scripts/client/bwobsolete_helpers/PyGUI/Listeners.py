# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Listeners.py

import weakref

# A global list to store weak references of all registered input language change listeners
_languageChangeListeners = []

# A global list to store weak references of all registered device listeners
_deviceListeners = []

# This function registers a new input language change listener
def registerInputLangChangeListener(listener):
    global _languageChangeListeners
    _languageChangeListeners.append(weakref.ref(listener))


# This function registers a new device listener
def registerDeviceListener(listener):
    _deviceListeners.append(weakref.ref(listener))


# This function handles the input language change event by calling the handleInputLangChangeEvent method
# of all registered input language change listeners (if available)
def handleInputLangChangeEvent():
    import GUI
    for listener in [x() for x in _languageChangeListeners if x() is not None]:
        if hasattr(listener, 'handleInputLangChangeEvent'):
            listener.handleInputLangChangeEvent()

    return True


# This function calls the onRecreateDevice method of all registered device listeners (if available)
def onRecreateDevice():
    for listener in [x() for x in _deviceListeners if x() is not None]:
        if hasattr(listener, 'onRecreateDevice'):
            listener.onRecreateDevice()

    return

