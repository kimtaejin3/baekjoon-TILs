# https://www.acmicpc.net/problem/14503
N, M = map(int, input().split())
x, y, d = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

mapper = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def all_clean(x, y):
    clean = True
    for i in range(4):
        dx, dy = mapper[i]

        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            if grid[nx][ny] == 0:
                clean = False

    return clean

def simulate():
    global x, y, d

    while True:
        grid[x][y] = 2

        if all_clean(x, y):
            nx, ny = x - mapper[d][0], y - mapper[d][1]
            
            if grid[nx][ny] != 1:
                x, y = nx, ny
                continue
            else: 
                break
            
        d = d - 1
        if d == -1:
            d = 3 

        nx, ny = x + mapper[d][0], y + mapper[d][1]

        if grid[nx][ny] == 0:
            x, y = nx, ny


simulate()
# print('==')
cnt = 0
for i in range(N):
    for j in range(M):
        # print(grid[i][j], end=' ')
        if grid[i][j] == 2:
            cnt += 1
    # print()
print(cnt)