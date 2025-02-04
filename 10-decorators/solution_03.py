# implement a decorator that caches the return values of a function , so that when it's called with the same arguments , the cached value id returned instead of re-executing the function
import time


def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result =   func(*args)
        return result
    return wrapper 

@cache
def long_runing_function(a , b):
    time.sleep(4)
    return a +b 

print(long_runing_function(2,3))
print(long_runing_function(2,3))
print(long_runing_function(23,45))