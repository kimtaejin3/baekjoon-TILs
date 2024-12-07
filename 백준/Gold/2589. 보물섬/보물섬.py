from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().strip()) for _ in range(N)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

coordinates = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 'L']

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(start):

    visited = [[False] * M for _ in range(N)]
    step = [[0] * M for _ in range(N)]
    x, y = start
    q = deque([(x, y)])
    visited[x][y] = True
    max_distance = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                max_distance = max(max_distance, step[nx][ny])
                q.append((nx, ny))

    return max_distance

max_time = 0
for coord in coordinates:
    max_time = max(max_time, bfs(coord))

print(max_time)
