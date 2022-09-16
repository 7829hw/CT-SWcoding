def solve(n, m, A, B, C):
    D = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            D[i][j] = A[i][j] + B[i][j] - C[i][j]
    return D

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(N)]
D = solve(N, M, A, B, C)
for i in range(N):
    print(" ".join(map(str, D[i])))