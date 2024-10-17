n, m = tuple(map(int, input().split()))

dp = [
    [0]+ list(map(int, input().split()))
    for _ in range(n)
]

dp.insert(0, [0 for _ in range(m + 1)])

for x in range(1,n + 1):
    for y in range(1,m + 1):
        dp[x][y] += max(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])

print(dp[n][m])

