from collections import deque

M, N, H = map(int, input().split())

grid = []
for _ in range(H):
    grid.append(
        [
            list(map(int ,input().split()))
            for _ in range(N)
        ]
    )

visited = [
    [
        [False for _ in range(M)]
        for _ in range(N)
    ]
    for _ in range(H)
]

steps = [
    [
        [0 for _ in range(M)]
        for _ in range(N)
    ]
    for _ in range(H)
]

tomato_positions = []

for h in range(H):
    for n in range(N):
        for m in range(M):
            if grid[h][n][m] == 1:
                tomato_positions.append((h, n, m))

def in_range(h, x, y):
    return 0 <= h < H and 0 <= x < N and 0 <= y < M

dhs, dxs, dys = [-1, 1, 0, 0, 0, 0] ,[0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque(tomato_positions[:])
    
    for tomato_position in tomato_positions:
        h, x, y = tomato_position
        visited[h][x][y] = True
        steps[h][x][y] = 1
    
    while q:
        h, x, y = q.popleft()

        for dh, dx, dy in zip(dhs, dxs, dys):
            
            nh, nx, ny = h + dh, x + dx, y + dy
            if in_range(nh, nx, ny) and not visited[nh][nx][ny] and grid[nh][nx][ny] == 0:
                visited[nh][nx][ny] = True
                steps[nh][nx][ny] = steps[h][x][y] + 1
                q.append((nh, nx, ny))


bfs()
max_val = -1
is_zero_exist = False

for h in range(H):
    for n in range(N):
        for m in range(M):
            if steps[h][n][m] == 0 and grid[h][n][m] != -1:
                is_zero_exist = True
                break
            max_val = max(steps[h][n][m], max_val)

if is_zero_exist:
    print(-1)
else:
    print(max_val-1)
    



