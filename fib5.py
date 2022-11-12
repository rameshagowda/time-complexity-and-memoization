# Dynamic programming / Memoization (Cache) - It is all about introducing Cache / lru_cache (built-in)
# lru_cache from functools lru = least recently used cache
# https://www.youtube.com/watch?v=Qk0zUZW-U_M&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=18
# This significantly reduces the time complexity of the algorithm from exponential O(2n) to linear O(n).
# https://www.youtube.com/watch?v=v1SYihb4rcw
# https://www.youtube.com/watch?v=wjDY5RbILno

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


print("Fibonacci series is..")
for n in range(1, 40):
    print(n, ":", fibonacci(n))
