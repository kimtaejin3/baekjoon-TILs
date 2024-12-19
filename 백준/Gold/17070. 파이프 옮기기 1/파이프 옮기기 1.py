# https://www.acmicpc.net/problem/17070

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            continue
        if j > 0:
            if grid[i][j-1] != 1:
                dp[0][i][j] += dp[2][i][j-1] + dp[0][i][j-1]
        if i > 0:
            if grid[i-1][j] != 1:
                dp[1][i][j] += dp[2][i-1][j] + dp[1][i-1][j]
        if i > 0 and j > 0:
            if grid[i][j-1] != 1 and grid[i-1][j] != 1:
                dp[2][i][j] += dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])

# for i in range(N):
#     for j in range(N):
#         print(dp[0][i][j], end=' ')
#     print()
# print('==')
# for i in range(N):
#     for j in range(N):
#         print(dp[1][i][j], end=' ')
#     print()
# print('==')
# for i in range(N):
#     for j in range(N):
#         print(dp[2][i][j], end=' ')
#     print()
