#!/usr/bin/python3
""" LIFO Caching"""
from base_caching import BaseCaching
class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching
    and is a caching system"""
    def __init__(self):
        super().__init__()
        self.lifo = []
    
    def put(self, key, item):
        """Must assign to the dictionary """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.lifo.pop()
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.lifo.append(key)
            self.cache_data[key] = item

    
    def get(self, key):
        """Must return the value in self.cache_data"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
