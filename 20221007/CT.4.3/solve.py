def sumofdigit(S):
    S = list(str(S))
    S = map(int, S)
    return sum(S)

def solve(N, M):
    cnt = 0
    for i in range(N, M + 1):
        tmp = sumofdigit(i)
        if int(tmp ** 0.5) ** 2 == tmp:
            cnt += 1
    return cnt

N, M = map(int, input().split())

print(solve(N, M))