# https://www.acmicpc.net/problem/10026
import sys
sys.setrecursionlimit(10**6)

N = int(input())

grid = [
    list(input())
    for _ in range(N)
]

visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def initialize_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

def dfs(x, y, color, is_red_green_blindness):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if not in_range(nx, ny):
            continue

        if visited[nx][ny]:
            continue
        
        if is_red_green_blindness and (color == "R" or color == "G"):
            if grid[nx][ny] == "R" or grid[nx][ny] == "G":
                visited[nx][ny] = True
                dfs(nx, ny, color, is_red_green_blindness)
        else:
            if grid[nx][ny] == color:
                visited[nx][ny] = True
                dfs(nx, ny, color, is_red_green_blindness)

cnt_nomarl = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_nomarl += 1
            visited[i][j] = True
            dfs(i, j, grid[i][j], False)

initialize_visited()

cnt_blindness = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_blindness += 1
            visited[i][j] = True
            dfs(i, j, grid[i][j], True)

print(cnt_nomarl, cnt_blindness)

