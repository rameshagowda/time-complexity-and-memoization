# Dynamic programming / Memoization (Cache) - It is all about introducing Cache / lru_cache (built-in)
# Explicitly introducing Cache
# https://www.youtube.com/watch?v=Qk0zUZW-U_M&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=18
# This significantly reduces the time complexity of the algorithm from exponential O(2^n) to linear O(n).
# https://www.youtube.com/watch?v=v1SYihb4rcw
# https://www.youtube.com/watch?v=wjDY5RbILno

fibonacci_cache = {}  # Dictionary


def fibonacci(n):
    # print('calculating term - {0}'.format(n))
    # If there is a cached value, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term, cache it and return
    if n == 1:
        value = 0
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


print("Fibonacci series is..")
for n in range(1, 40):
    print(n, ":", fibonacci(n))
