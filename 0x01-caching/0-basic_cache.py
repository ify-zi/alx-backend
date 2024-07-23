#!/usr/bin/env python3
"""
    Simple cahing method which inherits a base class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        Basic class that inherit BaseCaching class
        with added methods
    """

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """insertion function into the cache"""
        if key or item is None:
            self.cache_data[str(key)] = item
        return

    def get(self, key):
        """
            returns value of key if key exist
        """
        if key is not None:
            for idx, value in self.cache_data.items():
                if idx == key:
                    return value
        return None
