n = int(input())

grid = [
    list(map(int, input()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
houses = []
town = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global house

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            house += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            town += 1
            house = 1
            dfs(i, j)
            houses.append(house)


# print('town:',town)
# print('houses:', houses)

print(town)
for house in sorted(houses):
    print(house)
