#!/usr/bin/env python3
"""
Task: Advance Task
"""
import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis connection
redis_store = redis.Redis(host='localhost', port=6379, db=0)

def data_cacher(method: Callable) -> Callable:
    @wraps(method)
    def invoker(url) -> str:
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        # Set cache with a 10-second expiration
        redis_store.setex(f'result:{url}', 10, result)
        return result

    return invoker

@data_cacher
def get_page(url: str) -> str:
    return requests.get(url).text

if __name__ == "__main__":
    # Example usage
    page_content = get_page('http://slowwly.robertomurray.co.uk/delay/10000/url/http://www.example.com')
    print(page_content)

