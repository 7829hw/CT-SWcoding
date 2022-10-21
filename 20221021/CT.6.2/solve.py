from operator import mod


def modular(S, N, M):
    for i in range(N):
        for j in range(N):
            S[i][j] = S[i][j] % M
    return S

def calc(A, B, N):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range (N):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

def solve(A, N, M, P):
    if P == 1:
        # A = modular(A, N, M)
        return A
    t2 = solve(A, N, M, P // 2)
    temp = calc(t2, t2, N)
    # temp = modular(temp, N, M)

    temp = calc(temp, temp, N)
    # temp = modular(temp, N, M)
    if P % 2 == 1:
        temp = calc(temp, A, N)
        temp = modular(temp, N, M)
        return temp
    else:
        temp = modular(temp, N, M)
        return temp

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M , P = map(int, input().split())
for i in solve(A, N, M, P):
    print(" ".join(list(map(str, i))))