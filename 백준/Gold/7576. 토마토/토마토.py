from collections import deque

m, n = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

steps = [
    [0 for _ in range(m)]
    for _ in range(n)
]

start_idxs  = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    q = deque(start_idxs)
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for x, y in q:
        steps[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and grid[nx][ny] == 0 and steps[nx][ny] == 0:
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))


bfs()

for i in range(n):
    for j in range(m):
        if grid[i][j] == -1:
            steps[i][j] = -1

max_val = -1
for i in range(n):
    for j in range(m):
        max_val = max(max_val, steps[i][j])
        if steps[i][j] == 0:
            print(-1)
            exit(0)


print(max_val - 1)

    
