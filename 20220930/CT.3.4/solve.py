import sys
input = sys.stdin.readline

N = int(input())

M = list(map(int, input().split()))

result = []

for i in range(N):
    if M[i] == i + 1:
        result += [i + 1]

result.sort()

print(len(result))
print(" ".join(map(str, result)))