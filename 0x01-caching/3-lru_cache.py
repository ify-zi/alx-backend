#!/usr/bin/env python3
"""
    Using the LRU algorithm
    to caching data with a max_num of items
    inherited from base class
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRU cache class that inherit BaseCaching class
        with put method using LIFO algorithm
    """

    def __init__(self):
        """constructor method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            insertion function into the cache
            but with max_item of 4 and using the
            LRU algorithm
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
            returns value of key if key exist
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
