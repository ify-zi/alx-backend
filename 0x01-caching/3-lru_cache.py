#!/usr/bin/env python3
"""
    Using the LRU algorithm
    to caching data with a max_num of items
    inherited from base class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRU cache class that inherit BaseCaching class
        with put method using LIFO algorithm
    """

    def __init__(self):
        """constructor method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
            insertion function into the cache
            but with max_item of 4 and using the
            LRU algorithm
        """
        cache = self.cache_data
        if (key is None or item is None):
            pass
        if (len(cache) >= BaseCaching.MAX_ITEMS and key not in cache):
            print('DISCARD: {}'.format(self.keys[0]))
            cache.pop(self.keys.pop(0))

        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        cache[key] = item

    def get(self, key):
        """
            returns value of key if key exist
        """
        if (key is None or key not in self.cache_data.keys()):
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
