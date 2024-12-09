import sys
# Recursion Error 방지- 재귀의 한도 10000까지 풀어주기
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())

grid = [
    [0 for _ in range(N)]
    for _ in range(M)
]

visited = [
    [False for _ in range(N)]
    for _ in range(M)
]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = -1

dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(y, x):
    return 0 <= y < M and 0 <= x < N

def dfs(y, x):
    global temp
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if in_range(ny, nx) and not visited[ny][nx] and grid[ny][nx] == 0:
            visited[ny][nx] = True
            temp += 1
            dfs(ny, nx)

ans = []
for y in range(M):
    for x in range(N):
        if grid[y][x] == 0 and not visited[y][x]:
            temp = 1
            visited[y][x] = True
            dfs(y, x)
            ans.append(temp)


ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))

