# Fibonacci Series

# Approach - 1 - Using number of terms
def fib(a, b, n):
    if n == 0:
        return 0
    else:
        print(a, b, end=' ')
        a = a + b
        b = b + a
        n -= 2
        return fib(a, b, n)

fib(0, 1, 20)

# Approach - 2 - Using last term
def fibo(a, b, n):
    if b > n:
        print (a)
        return 0
    else:
        print(a, b, end=' ')
        a = a + b
        b = b + a
        return fibo(a, b, n)

fibo(0, 1, 9)