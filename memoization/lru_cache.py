import functools
import timeit

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

time2 = timeit.timeit('fibonacci(35)', globals=globals(), number=1)
print(time2)

time2 = timeit.timeit('fibonacci(35)', globals=globals(), number=1)
print(time2)
