import sys

INT_MAX = sys.maxsize

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

dp = [INT_MAX] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    for j in range(len(coins)):
        if i - coins[j] >= 0:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[k] == INT_MAX:
    print(-1)
else:
    print(dp[k])