def solve(N):
    print(N, end = " ")
    s = str(N)
    if len(s) == 1:
        return N
    else:
        M = 1
        for i in range(len(s)):
            M *= int(s[i])
        return solve(M)

N = int(input())
print(solve(N))