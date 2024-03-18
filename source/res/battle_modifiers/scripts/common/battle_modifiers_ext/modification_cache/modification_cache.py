import collections
from typing import Optional, Any

class ModificationCache:
    """
    A class that caches modifications in separate layers, with the ability to
    automatically remove the oldest layer when the maximum layer count is reached.
    """
    DEFAULT_LAYER_COUNT = 10  # The default maximum layer count

    __slots__ = ('_modifications', '_max_layer_count', '_layer_id_queue')

    def __init__(self, layer_count: Optional[int] = None):
        """
        Initializes the ModificationCache instance with the specified layer_count.
        If layer_count is None, the DEFAULT_LAYER_COUNT will be used.

        :param layer_count: The maximum number of layers to keep in the cache
        """
        if layer_count is None:
            layer_count = self.DEFAULT_LAYER_COUNT
        self._modifications = {}  # A dictionary to store modifications by layer id
        self._max_layer_count = layer_count  # The maximum number of layers allowed
        self._layer_id_queue: collections.deque[int] = collections.deque()  # A queue to store layer ids

    def clear(self):
        """
        Clears all modifications and layer ids from the cache.
        """
        self._modifications.clear()
        self._layer_id_queue.clear()

    def _add_layer(self, layer_id: int, init_value: Optional[Any] = None):
        """
        Adds a new layer with the given layer_id to the cache.
        If the maximum layer count is reached, the oldest layer will be removed.

        :param layer_id: The id of the layer to add
        :param init_value: The initial value for the new layer (optional)
        """
        if len(self._layer_id_queue) == self._max_layer_count:
            layer_id_to_remove = self._layer_id_queue.popleft()
            del self._modifications[layer_id_to_remove]
        self._layer_id_queue.append(layer
