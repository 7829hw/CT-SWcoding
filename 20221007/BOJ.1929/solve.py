def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def solve(M, N):
    cnt = 0
    for i in range(M, N + 1):
        if is_prime(i):
            cnt += 1
    return cnt

M, N = map(int, input().split())
print(solve(M, N))