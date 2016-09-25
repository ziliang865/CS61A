def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
from timeit import repeat
print(repeat('fib(20)','from __main__ import fib',number=10))