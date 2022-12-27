N = int(input())

s = {}

for i in range(N):
    f = input().strip()
    k = str(sorted(f))
    if k not in s.keys():
        s[k] = []
        s[k].append(f)
    else:
        s[k].append(f)
        s[k].sort()

s = sorted(s.items(), key=lambda x: (x[1][0]))

for j in range(len(s)):
    v = s[j][1]
    print(*v)