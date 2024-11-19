import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, input().split())

grid = [
    [0 for _ in range(M)]
    for _ in range(N)
]
visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

for _ in range(K):
    n, m = map(int, input().split())
    grid[n-1][m-1] = 1

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(n, m):
    return 0 <= n < N and 0 <= m < M

def dfs(x, y):
    global size
    
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            size += 1
            dfs(nx, ny)

ans = -1
for n in range(N):
    for m in range(M):
        if not visited[n][m] and grid[n][m] == 1:
            size = 1
            dfs(n, m)
            ans = max(size, ans)

print(ans)
