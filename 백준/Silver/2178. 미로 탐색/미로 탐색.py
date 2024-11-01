from collections import deque

N, M = map(int, input().split())

grid = [
    list(map(int, input()))
    for _ in range(N)
]

visited = [
    [0 for _ in range(M)]
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(x, y):
    q = deque([(x, y)])
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        curr_num = visited[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue
            
            if grid[nx][ny] == 0:
                continue

            if visited[nx][ny] != 0:
                continue
            
            visited[nx][ny] = curr_num + 1
            q.append((nx, ny))

bfs(0, 0)

print(visited[N-1][M-1])
