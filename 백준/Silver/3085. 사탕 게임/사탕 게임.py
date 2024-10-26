import sys
input = sys.stdin.readline

N = int(input())

grid = [
    list(input())
    for _ in range(N)
]

ans = -1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def find_max():
    max_cnt = 0

    for i in range(N):
        cnt_h, cnt_v = 1, 1
        for j in range(N-1):
            if grid[i][j] == grid[i][j+1]:
                cnt_h += 1
            # 이 부분을 처리 안해서 8%에서 계속 틀림
            else:
                max_cnt = max(max_cnt, cnt_h)
                cnt_h = 1
        
        for j in range(N-1):
            if grid[j][i] == grid[j+1][i]:
                cnt_v += 1
            # 이 부분을 처리 안해서 8%에서 계속 틀림
            else:
                max_cnt = max(max_cnt, cnt_v)
                cnt_v = 1

        max_cnt = max(max_cnt, cnt_h, cnt_v)

    return max_cnt

def swap_and_move(n, m):
    global ans

    dxs, dys = [1, 0], [0, 1]
    target_n, target_m = -1, -1
    
    for dx, dy in zip(dxs, dys):
        nx, ny = n + dx, m + dy

        if in_range(nx, ny) and grid[nx][ny] != grid[n][m]:
            target_n, target_m = nx, ny
            temp = grid[n][m]
            grid[n][m] = grid[target_n][target_m]
            grid[target_n][target_m] = temp

            ans = max(ans, find_max())
            
            temp = grid[n][m]
            grid[n][m] = grid[target_n][target_m]
            grid[target_n][target_m] = temp
            

def simulate():
    for n in range(N):
        for m in range(N):
            swap_and_move(n, m)

simulate()
print(ans)
