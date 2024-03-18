# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/DestructibleStickers.py

import BigWorld  # Import BigWorld for creating and managing sticker models
import math_utils  # Import math_utils for creating an identity matrix
import VehicleStickers  # Import VehicleStickers for DamageSticker class

class DestructibleStickers(object):
    """
    A class representing destructible stickers for a vehicle model.
    """

    def __init__(self, spaceID, model, nodeToAttach):
        """
        Initialize the DestructibleStickers object with a space ID, a vehicle model, and a node to attach the sticker model.

        :param spaceID: The space ID for the sticker model.
        :param model: The vehicle model to attach the sticker model to.
        :param nodeToAttach: The node to attach the sticker model to on the vehicle model.
        """
        self.__model = model  # Store the vehicle model
        self.__stickerModel = BigWorld.WGStickerModel(spaceID)  # Create a sticker model with the given space ID
        self.__stickerModel.setLODDistance(1000.0)  # Set the LOD distance for the sticker model
        self.__stickerModel.setupSuperModel(model, math_utils.createIdentityMatrix())  # Set up the sticker model with the vehicle model and an identity matrix
        self.__nodeToAttach = nodeToAttach  # Store the node to attach the sticker model to
        nodeToAttach.attach(self.__stickerModel)  # Attach the sticker model to the specified node
        self.__damageStickers = {}  # Initialize an empty dictionary for storing damage stickers

    def destroy(self):
        """
        Destroy the DestructibleStickers object and its associated resources.

        """
        if self.__model is None:
            return
        else:
            if self.__stickerModel.attached and self.__nodeToAttach is not None:
                self.__nodeToAttach.detach(self.__stickerModel)  # Detach the sticker model from the node
            self.__stickerModel.clear()  # Clear the sticker model
            self.__damageStickers.clear()  # Clear the damage stickers dictionary
            return

    def addDamageSticker(self, code, stickerID, segStart, segEnd):
        """
        Add a damage sticker to the sticker model with the given parameters.

        :param code: A unique code for the damage sticker.
        :param stickerID: The ID of the sticker to add.
        :param segStart: The start of the segment for the sticker.
        :param segEnd: The end of the segment for the sticker.
        """
        if code in self.__dam
