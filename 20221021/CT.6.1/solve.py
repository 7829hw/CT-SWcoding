def matrix_multiplication(A, B, L, M, N):
    C = [[0]*N for _ in range(L)]
    for i in range(L):
        for j in range(N):
            for k in range (M):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

def solve(A, B, L, M, N):
    C = matrix_multiplication(A, B, L, M, N)
    for i in C:
        print(" ".join(map(str, i)))



L, M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(L)]
B = [list(map(int, input().split())) for _ in range(M)]

solve(A, B, L, M, N)