#!/usr/bin/env python3

import redis
from uuid import uuid4, UUID
from typing import Union

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
