def solve(n, m):
    s = 0
    for i in range(n, m+1):
        s += i
    return s


N = int(input())
M = int(input())
S = solve(N, M)
print(S)