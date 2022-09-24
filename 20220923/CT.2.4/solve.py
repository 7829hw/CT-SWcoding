def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3*n + 1)

N = int(input())
print(collatz(N))
print(max(collatz(N)))