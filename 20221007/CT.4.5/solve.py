def solve(N, M):
    cnt = 0
    for i in M:
        a = sorted(list(i))
        if N == a:
            cnt += 1
    return cnt



N = list(input())
M = input().split()

print(solve(N, M))