#!/usr/bin/env python3

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

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
    
    
def count_calls(method: Callable = None) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        name = method.__qualname__
        self._redis.incrby(name, 1)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator call history """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wraper function """
        input: str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper
