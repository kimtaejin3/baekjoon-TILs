N = int(input())

grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]

arr = [
    list(map(int, input().split()))
    for _ in range(N * N)
]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
def check_cells(a):
    
    selected_x, selected_y = -1, -1
    liked = -1
    empty = -1

    for x in range(N):
        for y in range(N):
            if grid[x][y] != 0:
                continue
            temp_liked, temp_empty = 0, 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if not in_range(nx, ny):
                    continue

                if grid[nx][ny] == 0:
                    temp_empty += 1

                if grid[nx][ny] in a[1:]:
                    temp_liked += 1    
            
            if liked < temp_liked:
                liked = temp_liked
                empty = temp_empty

                selected_x, selected_y = x, y
            elif liked == temp_liked:
                if empty < temp_empty:
                    empty = temp_empty
                    selected_x, selected_y = x, y
                
            
    
    # print('selected:',selected_x, selected_y, liked, empty)
    return selected_x, selected_y


for i in range(N * N):
    x, y = check_cells(arr[i][:])
    grid[x][y] = arr[i][0]

# for x in range(N):
#     for y in range(N):
#         print(grid[x][y], end=' ')
#     print()

ans = 0

for i in range(len(arr)):
    me, others = arr[i][0], arr[i][1:]

    for x in range(N):
        for y in range(N):
            if grid[x][y] != me:
                continue
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if not in_range(nx, ny):
                    continue
                    
                if grid[nx][ny] in others:
                    cnt += 1
            
            if cnt == 1:
                ans += 1
            elif cnt == 2:
                ans += 10
            elif cnt == 3:
                ans += 100
            elif cnt == 4:
                ans += 1000

print(ans)

