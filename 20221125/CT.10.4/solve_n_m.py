def maze(n, m, s):
    f = [[0] * m for _ in range(n)]

    for i in range(n):
        if i == 0:
            f[i][0] = s[i][0]
        else:
            f[i][0] = s[i][0] + f[i - 1][0]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                f[j][i] = s[j][i] + f[j][i-1]
            elif f[j][i-1] > f[j - 1][i]:
                f[j][i] = f[j - 1][i] + s[j][i]
            else:
                f[j][i] = f[j][i-1] + s[j][i]

        # for k in range(n):
        #     f[k][0] = f[k][1]
        #     f[k][1] = 0

    return f[n - 1][m-1]


N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

print(maze(N, M, S))
