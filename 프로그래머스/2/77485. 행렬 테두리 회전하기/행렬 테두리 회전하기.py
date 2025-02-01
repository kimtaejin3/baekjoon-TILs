def rotate(x1, y1, x2, y2, grid):
    arr = []
    
    for y in range(y1, y2):
        arr.append(grid[x1][y])
    
    for x in range(x1 + 1, x2):
        arr.append(grid[x][y2 - 1])
    
    for y in range(y2 - 2, y1 - 1, -1):
        arr.append(grid[x2 - 1][y])
    
    for x in range(x2 - 2, x1, -1):
        arr.append(grid[x][y1])
    
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        
    index = 0
    for y in range(y1, y2):
        grid[x1][y] = arr[index]
        index += 1

    for x in range(x1 + 1, x2):
        grid[x][y2 - 1] = arr[index]
        index += 1

    for y in range(y2 - 2, y1 - 1, -1):
        grid[x2 - 1][y] = arr[index]
        index += 1

    for x in range(x2 - 2, x1, -1):
        grid[x][y1] = arr[index]
        index += 1
    
    return min(arr)
    
def solution(rows, columns, queries):
    grid = [
        [0 for _ in range(columns)]
        for _ in range(rows)
    ]
    
    cnt = 1
    for row in range(rows):
        for col in range(columns):
            grid[row][col] = cnt
            cnt += 1
    
    res = []
    
    for query in queries:
        x1, y1, x2, y2 = query
        
        min_val = rotate(x1 - 1, y1 - 1, x2, y2, grid)
    
        res.append(min_val)
     
    return res