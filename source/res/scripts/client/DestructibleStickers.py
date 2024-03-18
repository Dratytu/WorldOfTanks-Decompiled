    def updateDamageSticker(self, code, stickerID=None, segStart=None, segEnd=None):
        """
        Update a damage sticker in the sticker model with the given parameters.

        :param code: A unique code for the damage sticker.
        :param stickerID: The ID of the sticker to update (optional).
        :param segStart: The start of the segment for the sticker (optional).
        :param segEnd: The end of the segment for the sticker (optional).
        """
        if code in self.__damageStickers:
            damageSticker = self.__damageStickers[code]
            if stickerID is not None:
                damageSticker.stickerID = stickerID
            if segStart is not None:
                damageSticker.segStart = segStart
            if segEnd is not None:
                damageSticker.segEnd = segEnd
        else:
            self.addDamageSticker(code, stickerID, segStart, segEnd)

    def removeDamageSticker(self, code):
        """
        Remove a damage sticker from the sticker model with the given code.

        :param code: A unique code for the damage sticker.
        """
        if code in self.__damageStickers:
            del self.__damageStickers[code]

