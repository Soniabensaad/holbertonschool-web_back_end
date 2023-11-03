#!/usr/bin/env python3
"""Tasks"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    """Method"""
    def __init__(self):
        """self"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store"""
        random = str(uuid4())
        self._redis.set(random, data)
        return random

    def get(self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """get function"""
        find = self._redis.get(key)
        if find is not None:
            if fn is not None:
                return fn(find)
            else:
                return find
        return None

    def get_str(self, key: str) -> str:
        """get str function"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """get int function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value


def count_calls(method: Callable = None) -> Callable:
    """count calls"""
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call hystory"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input_str)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(self, method: Callable):
    """replay"""
    method_name = method.__qualname__
    inputs = self._redis.lrange(f"{method_name}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_str, output in zip(inputs, outputs):
        input_args = eval(input_str)
        print(f"{method_name}({input_args}) -> {output}")
