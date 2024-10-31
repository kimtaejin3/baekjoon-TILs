def search(lev):
	global row, col, square, matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9):
			for j in range(9):
				print(matrix[i][j], end=' ')
			print()
		exit(0)

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if (not row[y][n]) and (not col[x][n]) and (not square[y // 3][x // 3][n]):
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = True
			matrix[y][x] = n

			search(lev + 1)

			matrix[y][x] = 0
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = False


#initial settings
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[[False] * 10 for _ in range(3)] for _ in range(3)]

# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
	for j in range(9):
		cur = matrix[i][j]
		if cur == 0:
			pos.append((i, j))
		else:
			row[i][cur] = col[j][cur] = square[i // 3][j // 3][cur] = True

search(0)
