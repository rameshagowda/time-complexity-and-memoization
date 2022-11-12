# Iterative method
# Time complexity O(n)
# https://www.youtube.com/watch?v=v1SYihb4rcw
# https://www.youtube.com/watch?v=wjDY5RbILno

n0 = 0
n1 = 1


print("Fibonacci series is..")
for n in range(1, 101):
    print(n, ":", n0)
    n2 = n0+n1
    n0 = n1
    n1 = n2
