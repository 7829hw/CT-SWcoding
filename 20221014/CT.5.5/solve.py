def primes(n):
    sieve = [False, False] + [True] * (n - 1)
    P = []
    for i in range(2, n + 1):
        if sieve[i]:
            P.append(i)
            for j in range(2*i, n + 1, i):
                sieve[j] = False
    return P

def binsearch(N, P):
    low = 0
    high = len(P) - 1
    while low <= high:
        mid = (low + high) // 2
        if N > P[mid]:
            low = mid + 1
        elif N < P[mid]:
            high = mid - 1
        else:
            return mid + 1
    return -1

def solve(N, P):
    for i in range(len(N)):
        print(binsearch(N[i], P))
        

T = int(input())
N = [int(input()) for _ in range(T)]

P = primes(5000000)
solve(N, P)