def solve(N):
    sum = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            sum += i
            sum += N / i
    if int(N ** 0.5)**2 == N:
        sum -= int(N ** 0.5)
    return int(sum)

N = int(input())
print(solve(N))