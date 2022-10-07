def divisor(N):
    cnt = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            cnt += 2
    if int(N ** 0.5)**2 == N:
        cnt -= 1
    return cnt

def solve(N, M):
    a = 0
    b = 0
    for i in range(N, M + 1):
        if divisor(i) >= b:
            a = i
            b = divisor(i)
    return a, b

N, M = map(int, input().split())
x, y = solve(N, M)
print(x)
print(y)