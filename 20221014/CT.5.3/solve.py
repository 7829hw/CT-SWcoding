def solve(S):
    low = 0
    high = len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid > S[mid]:
            low = mid + 1
        elif mid < S[mid]:
            high = mid - 1
        else:
            return S[mid]
    return -1

N = int(input())
S = [int(input()) for _ in range(N)]

print(solve(S))