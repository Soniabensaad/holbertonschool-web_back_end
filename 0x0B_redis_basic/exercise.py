#!/usr/bin/env python3

import redis
from uuid import uuid4
from typing import Union, Callable, Optional

"""0. Writing strings to Redis"""
class Cache:
    """redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random = str(uuid4())
        self._redis.set(random, data)
        return random
    
    def get(self, key: str, fn: Callable=None) -> Union[str, bytes, int, float]:
        find = self._redis.get(key)
        if find is not None:
            if fn is not None:
                return fn(find)
            else:
                return find
        return None
    def get_str(self, key: str) -> str:
        return self._redis.get(key).decode("utf-8")
    
    def get_int(self, key: str) -> int:
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0

        return value
    
    def __init__(self):
        self.cache = {}

    def store(self, key, value):
        self.cache[key] = value

    def retrieve(self, key):
        return self.cache.get(key, None)

    def count_calls(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Use the qualified name of the method as the key
            key = method.__qualname__

            # Increment the call count
            self.store(key, self.retrieve(key, 0) + 1)

            # Call the original method and return its result
            return method(self, *args, **kwargs)

        return wrapper
