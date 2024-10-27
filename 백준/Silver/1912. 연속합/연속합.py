N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for n in range(1, N + 1):
    dp[n] = max(dp[n-1], 0) + arr[n]

print(max(dp[1:]))

