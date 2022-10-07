import math

def solve(M, N):
    sieve = [1] * (N + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i] >= 0:
            for j in range(i * i, N + 1, i):
                sieve[j] = 0
    print(sieve)
    return sum(sieve)

M, N = map(int, input().split())
print(solve(M, N))