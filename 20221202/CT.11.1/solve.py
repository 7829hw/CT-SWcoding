def dfs(v, G, visited, count):
    count += 1
    visited[v] = True
    if v == q:
        print(count - 1)
        # result.append(count)
    # print(v, end=" ")
    for u in G[v]:
        if not visited[u]:
            dfs(u, G, visited, count)


n, m = map(int, input().split())
p, q = map(int, input().split())
# print(n, m, p, q)
G = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * (n + 1)
# result = []
dfs(p, G, visited, 0)
# print(result[0]-1 if len(result)!=0 else -1)
