from collections import deque

N, M = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

virus = [
    (i, j)
    for i in range(N)
    for j in range(M)
    if grid[i][j] == 2
]

blanks = [
    (i, j)
    for i in range(N)
    for j in range(M)
    if grid[i][j] == 0
]

def init_visited():
    for n in range(N):
        for m in range(M):
            visited[n][m] = False

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs():
    q = deque(virus)
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for v in virus:
        x, y = v
        visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))

def get_safety_area_cnt():
    cnt = 0
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and grid[n][m] == 0:
                cnt += 1

    return cnt

choose_blanks = []

ans = -1
def choose(index, lev):
    global ans 

    if lev == 3:
        init_visited()

        for blank in choose_blanks:
            x, y = blank
            grid[x][y] = 1
        
        bfs()

        ans = max(get_safety_area_cnt(), ans)

        for blank in choose_blanks:
            x, y = blank
            grid[x][y] = 0

        return

    for i in range(index, len(blanks)):
        choose_blanks.append(blanks[i])
        choose(i + 1, lev + 1)
        choose_blanks.pop()

choose(0, 0)

print(ans)

