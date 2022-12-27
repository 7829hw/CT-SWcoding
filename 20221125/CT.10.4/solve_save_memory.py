def maze(n, m, s):
    f = [[0, 0] for _ in range(n)]

    f[0][0] = s[0][0]
    for i in range(1, n):
        f[i][0] = s[i][0] + f[i - 1][0]

    for i in range(1, m):
        f[0][1] = s[0][i] + f[0][0]
        for j in range(1, n):
            if f[j][0] > f[j - 1][1]:
                f[j][1] = f[j - 1][1] + s[j][i]
            else:
                f[j][1] = f[j][0] + s[j][i]

        for k in range(n):
            f[k][0] = f[k][1]
            # f[k][1] = 0

    return f[n - 1][0]


N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

print(maze(N, M, S))
