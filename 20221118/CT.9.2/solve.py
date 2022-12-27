N = int(input())

sell = {}
for i in range(N):
    fruit = input().strip()
    if fruit not in sell.keys():
        sell[fruit] = 1
    else:
        sell[fruit] += 1

sell = sorted(sell.items(), key=lambda x: (-x[1], x[0]))
for i in sell:
    print(i[1], i[0])
