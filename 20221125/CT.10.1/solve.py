def fib(n):
    if n < 2:
        return n
    else:
        a, b, c = 0, 1, 2
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


n = int(input())
print(fib(n))
