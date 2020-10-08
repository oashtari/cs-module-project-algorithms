# BOTTOMS UP SAMPLE SOLUTION FOR FIBONACCI TYPE PROBLEM

# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
#
# 0 1 1 2 3
#
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)
​
# Bottom-up dynamic programming
#
# Start from the base case and work up toward the number
​
def fib(n):
    f = [0, 1]
​
    if n <= 1:
        return f[n]
​
    for _ in range(n - 1):
        next_fib = f[-1] + f[-2]
        f.append(next_fib)
​
    return f[-1]
        
​
for i in range(0, 1000):
    print(f'{i:3} {fib(i)}')