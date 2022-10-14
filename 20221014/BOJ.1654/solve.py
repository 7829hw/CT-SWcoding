def possible(mid, A):
    cnt = 0
    for i in A:
        cnt += i // mid
    return cnt

def binsearch_recur(n, A, low, high):
    if low > high:
        return high
    else:
        mid = (low + high) // 2
        maxn = possible(mid, A)
        if n > maxn:
            return binsearch(n, A, low, mid - 1)
        else:
            return binsearch(n, A, mid + 1, high)

def binsearch(n, A, low, high):
    while low <= high:
        mid = (low + high) // 2
        maxn = possible(mid, A)
        if n > maxn:
            high = mid - 1
        else:
            low = mid + 1
    return high

def solve(n, A):
    return binsearch(n, A, 1, max(A))

K, N = map(int, input().split())
A = [int(input()) for _ in range(K)]

print(solve(N, A))