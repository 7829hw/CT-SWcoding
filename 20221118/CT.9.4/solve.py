def hor(n, m):
    cnt = 0
    pos = {}
    for i in m:
        if i[1] not in pos.keys():
            pos[i[1]] = 1
        else:
            pos[i[1]] += 1
    for i in list(pos.values()):
        if i > 1:
            cnt += 1
    return cnt


def ver(n, m):
    cnt = 0
    pos = {}
    for i in m:
        if i[0] not in pos.keys():
            pos[i[0]] = 1
        else:
            pos[i[0]] += 1
    for i in list(pos.values()):
        if i > 1:
            cnt += 1
    return cnt


n = int(input())

m = [tuple(map(int, input().split())) for _ in range(n)]

print(ver(n, m))
print(hor(n, m))
