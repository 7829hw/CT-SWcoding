idx = -1
def get_next(s):
    global idx
    idx += 1
    return s[idx]

def quadtree(i, j, n, s, T):
    head = get_next(s)
    if head == "W" or head == "B":
        for r in range(i, i + n):
            for c in range(j, j + n):
                T[r][c] = 0 if head == "W" else 1
    else:
        m = n // 2
        quadtree(i, j, m, s, T)
        quadtree(i, j + m, m, s, T)
        quadtree(i + m, j, m, s, T)
        quadtree(i + m, j + m, m, s, T)

    return T

def solve(N, S):
    T = [[0] * N for _ in range(N)]
    answer = quadtree(0, 0, N, S, T)
    for i in answer:
        print("".join(map(str, i)))

N = int(input())
S = input()

solve(N, S)