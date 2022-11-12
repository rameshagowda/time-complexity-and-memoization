# Iterative method with function
# https://www.youtube.com/watch?v=v1SYihb4rcw
# https://www.youtube.com/watch?v=wjDY5RbILno
def fibonacci(n):
    previous_num, current_num = 0, 1
    for n in range(1, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous_num, current_num = current_num, previous_num + current_num
        print(n, ":", current_num)


print("Fibonacci series is..")
fibonacci(5)
