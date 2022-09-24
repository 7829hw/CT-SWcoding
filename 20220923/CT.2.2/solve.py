from functools import reduce

def gcd(N, M):
    if M == 0:
        return N
    else:
        return gcd(M, N % M)

def lcm(N, M):
    return N * M // gcd(N, M)

N = int(input())
S = map(int, input().split())

print(reduce(lcm, S))