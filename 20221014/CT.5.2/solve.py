def solve(N, M, S):
    question = 0
    for i in range(len(S)):
        low = N
        high = M
        while low <= high:
            question += 1
            mid = (low + high) // 2
            if mid < S[i]:
                low = mid + 1
            elif mid > S[i]:
                high = mid - 1
            else:
                break
    return question


N, M = map(int, input().split())
K = int(input())
X = list(map(int, input().split()))

print(solve(N, M, X))