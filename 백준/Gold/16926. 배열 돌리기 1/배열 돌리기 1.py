N, M, R = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = [
    [False] * (M)
    for _ in range(N)
]

def init_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

count = 0
def roll(init_x, init_y, d):
    global count
    x, y = init_x, init_y
    temp = arr[x][y]
    visited[x][y] = True
    nx, ny = x + dxs[d], y + dys[d]
    
    while nx != init_x or ny != init_y:
        count += 1
        # print(x, y, nx, ny)
        # if count == 50:
            # break

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            arr[x][y] = arr[nx][ny]
            x, y = nx, ny
            visited[x][y] = True
            nx, ny = x + dxs[d], y + dys[d]
        else:
            d = (d + 1) % 4
            nx, ny = x + dxs[d], y + dys[d]

    # print(x, y, nx, ny)

    arr[init_x + 1][init_y] = temp

for _ in range(R):
    for i in range(min(N, M) // 2):
        roll(i, i, 0)
    
    init_visited()

# roll(0, 0, 0)
# roll(1, 1, 0)
# init_visited()
# roll(0, 0, 0)
# roll(1, 1, 0)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

