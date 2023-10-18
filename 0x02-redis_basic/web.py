#!/usr/bin/env python3

"""
import other files here
"""
import redis
import requests
from functools import wraps
from typing import Callable

"""
write the python class
"""

redis_store = redis.Redis()

"""
define the object here
"""

def data_cacher(method: Callable) -> Callable:
    @wraps(method)
    def invoker(url) -> str:
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    return requests.get(url).text
