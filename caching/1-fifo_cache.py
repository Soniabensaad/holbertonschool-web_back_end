#!/usr/bin/python3
"""  FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Create a class FIFOCache that inherits
    from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Must assign to the dictionary """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
