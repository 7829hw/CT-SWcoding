def solve(s, n):
    dp = [0] * 300
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(dp[0], dp[1]) + s[2]
    for i in range(3, n):
        dp[i] = max(dp[i - 2], dp[i - 1]) + s[i]
    return dp[n - 1]


n = int(input())
s = list(map(int, input().split()))
print(solve(s, n))
