def solve(n):
    circle, sequence = [i for i in range(1, n + 1)], []
    j = 0
    i = 1
    while len(circle) > 0:
        k = i**3
        j = (j + k - 1) % len(circle)
        sequence.append(circle.pop(j))
        i += 1
    return sequence[-1]


N = int(input())
print(solve(N))
