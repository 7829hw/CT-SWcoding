def is_prime(n):
    if n < 2:
        return False
    else:
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

def solve(N):
    cnt = 0
    i = 0
    while cnt < N:
        if is_prime(i):
            cnt += 1
        i += 1
    return i - 1


N = int(input())
print(solve(N))