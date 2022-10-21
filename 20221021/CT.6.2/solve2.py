N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M , P = map(int, input().split())

def calc(A, P, M):
    if P == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= M
        return A
    t2 = calc(A, P//2, M)

    tmp = [[0 for i in range(len(t2))] for i in range(len(t2))]
    for i in range(len(t2)):
        for j in range(len(t2)):
            for n in range(len(t2)):
                tmp[i][j] += t2[i][n] * t2[n][j]
                tmp[i][j] %= M
    if P % 2 == 1: 
        tmp2 = [[0 for i in range(len(t2))] for i in range(len(t2))]
        for i in range(len(t2)):
            for j in range(len(t2)):
                for n in range(len(t2)):
                    tmp2[i][j] += tmp[i][n] * A[n][j]
                    tmp2[i][j] %= M
        return tmp2
    else:
        return tmp

for i in calc(A, P, M):
    print(" ".join(list(map(str, i))))