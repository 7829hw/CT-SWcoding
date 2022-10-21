def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != chk:
                return 2
    return chk

def quadtree(i, j, n, A):
    if n == 1:
        return 'B' if A[i][j] else 'W'
    else:
        chk = check(i, j, n, A)
        if chk < 2:
            return 'B' if chk else 'W'
        else:
            m = n // 2
            s1 = quadtree(i, j, m, A)
            s2 = quadtree(i, j + m, m, A)
            s3 = quadtree(i + m, j, m, A)
            s4 = quadtree(i + m, j + m, m, A)
            return "Q" + s1 + s2 + s3 + s4

def solve(N, A):
    print(N)
    print(quadtree(0, 0, N, A))

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

solve(N, A)