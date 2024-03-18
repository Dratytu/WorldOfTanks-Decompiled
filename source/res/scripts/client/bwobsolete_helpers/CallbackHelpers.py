# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/CallbackHelpers.py

import BigWorld # Importing BigWorld, which might provide a base class or utility functions for game objects.

def IgnoreCallbackIfDestroyed(function):
    """
    A decorator that checks if the object is destroyed before calling the function.
    If the object is destroyed, the function will not be called and None will be returned instead.

    Parameters:
    function (callable): The function to decorate.

    Returns:
    callable: A new decorated function that checks if the object is destroyed before calling the original function.
    """

    def checkIfDestroyed(self, *args, **kwargs):
        """
        The new decorated function that checks if the object is destroyed before calling the original function.

        Parameters:
        self (object): The object on which the original function is called.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

        Returns:
        object: The result of the function call if the object is not destroyed, otherwise None.
        """
        return function(self, *args, **kwargs) if not self.isDestroyed else None

    return checkIfDestroyed # Return the new decorated function.

