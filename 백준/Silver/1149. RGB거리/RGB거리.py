# 백준 1149: 재귀로 풀고 아마 메모제이션 해야 되는 문데일듯.
# 이 문제는 백트래킹 같다..
# 어떤거에 메모제이션을 적용해야할지 모르겠음.
import sys

n = int(input())

dp = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1, n):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))
