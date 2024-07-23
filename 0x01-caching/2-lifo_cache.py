#!/usr/bin/env python3
"""
    Using the LIFO algorithm
    to caching data with a max_num of items
    nherited from base class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFO cache class that inherit BaseCaching class
        with put method using LIFO algorithm
    """

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """
            insertion function into the cache
            but with max_item of 4 and using the
            LIFO algorithm
        """
        data = []
        for i, v in self.cache_data.items():
            data.append(i)
        if key and item is not None:
            self.cache_data[str(key)] = item
            data_count = len(self.cache_data)
            if data_count > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.pop(data[-1], None)
                print("DISCARD: {}".format(data[-1]))

    def get(self, key):
        """
            returns value of key if key exist
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
