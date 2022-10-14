def fib(n):
    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F

def binsearch(N, F):
    low = 0
    high = 99999
    while low <= high:
        mid = (low + high) // 2
        if N > F[mid]:
            low = mid + 1
        elif N < F[mid]:
            high = mid - 1
        else:
            return mid
    return -1

def solve(N, F):
    for i in range(len(N)):
        print(binsearch(N[i], F))
        

T = int(input())
N = [int(input()) for _ in range(T)]

F = fib(100000)
solve(N, F)