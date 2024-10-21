a = input()
b = input()

n, m = len(a), len(b)

dp = [
    [0] + [0 for _ in range(m)]
    for _ in range(n)
]

dp.insert(0, [0 for _ in range(m+1)])

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for row in dp:
#     for elem in row:
#         print(elem, end=' ')
#     print()

print(dp[n][m])
