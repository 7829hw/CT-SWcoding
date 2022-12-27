from collections import deque


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque([(x, y, 1)])
    visited[x][y] = True
    while q:
        x, y, distance = q.popleft()
        if x == n - 1 and y == m - 1:
            print(distance - 1)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and not visited[nx][ny]
                    and graph[nx][ny] == 1
                ):
                    visited[nx][ny] = True
                    q.append((nx, ny, distance + 1))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

bfs(0, 0)
