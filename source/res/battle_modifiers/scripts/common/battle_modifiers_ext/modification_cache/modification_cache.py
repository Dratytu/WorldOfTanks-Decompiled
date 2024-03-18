import collections
from typing import Optional, Any

class ModificationCache:
    DEFAULT_LAYER_COUNT = 10
    __slots__ = ('_modifications', '_max_layer_count', '_layer_id_queue')

    def __init__(self, layer_count: Optional[int] = None):
        if layer_count is None:
            layer_count = self.DEFAULT_LAYER_COUNT
        self._modifications = {}
        self._max_layer_count = layer_count
        self._layer_id_queue: collections.deque[int] = collections.deque()

    def clear(self):
        self._modifications.clear()
        self._layer_id_queue.clear()

    def _add_layer(self, layer_id: int, init_value: Optional[Any] = None):
        if len(self._layer_id_queue) == self._max_layer_count:
            layer_id_to_remove = self._layer_id_queue.popleft()
            del self._modifications[layer_id_to_remove]
        self._layer_id_queue.append(layer_id)
        self._modifications[layer_id] = init_value

