from collections import deque

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, h):
    q = deque([(x, y)])
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))


ans = -1 
for h in range(101):
    init_visited()
    
    safety_area = 0

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and grid[x][y] > h:
                safety_area += 1
                visited[x][y] = True
                bfs(x, y, h)
    
    ans = max(ans, safety_area)

print(ans)
