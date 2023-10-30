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
    def get_int (self, key: str) -> int:
        value = self._redis.get(key)
        if value is not None:
           return int(value)
        return 0 
