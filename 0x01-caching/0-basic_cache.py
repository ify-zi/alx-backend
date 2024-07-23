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
        if key and item is not None:
            self.cache_data[str(key)] = item

    def get(self, key):
        """
            returns value of key if key exist
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
