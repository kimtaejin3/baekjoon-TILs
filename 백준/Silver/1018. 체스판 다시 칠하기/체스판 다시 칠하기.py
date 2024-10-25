n, m = map(int, input().split())
grid_w = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
grid_b = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]
input_grid = [
    input()
    for _ in range(n)
]

min_val = 64
for i in range(n):
    for j in range(m):
        end_i, end_j = i + 8, j + 8
        if end_i > n or end_j > m :
            continue
        
        cnt_b = 0
        cnt_w = 0

        for x in range(i, end_i):
            for y in range(j, end_j):
                if input_grid[x][y] != grid_b[x-i][y-j]:
                    cnt_b += 1
                elif input_grid[x][y] != grid_w[x-i][y-j]:
                    cnt_w += 1

        min_val = min(min_val, cnt_b, cnt_w)

print(min_val)
