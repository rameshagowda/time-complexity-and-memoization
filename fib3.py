# Recursion method
def fib(n):
    # print('calculating term - {0}'.format(n))
    # If we look at output, term-4 is calculated 2 times, term-3 is calculated 3 times, term-2 is calculated 5 times. We are making function call again and again just to calculate same thing. This is not good. This can be avoided by caching or memoizing already calculated term.
    # IMP: https://www.youtube.com/watch?v=AQp1OG7aSwg
    # To calculate F(5), fibonacci_of() has to call itself fifteen times. To calculate F(n), the maximum depth of the call tree is n, and since each function call produces two additional function calls, the time complexity of this recursive function is O(2n).
    # https://www.youtube.com/watch?v=wjDY5RbILno

    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)


print("Fibonacci series is..")
for n in range(1, 101):
    print(n, ":", fib(n))
