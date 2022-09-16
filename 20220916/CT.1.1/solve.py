def isleapyear(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def solve(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if isleapyear(i) == 1:
            cnt += 1
    return (b - a + 1) * 365 + cnt

A = int(input())
B = int(input())

print(solve(A, B))