def solve(n):
    sum = 0
    C = [0]*n
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum
    
N = int(input())

print(solve(N))