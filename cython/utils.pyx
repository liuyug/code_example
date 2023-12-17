#cython: language_level=3

cdef int Max(int x, int y):
    if x > y:
        return x
    else:
        return y


def hello(name):
    print(name)


def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
