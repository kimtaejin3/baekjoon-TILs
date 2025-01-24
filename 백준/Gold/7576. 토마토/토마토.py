from collections import deque

M, N = map(int, input().split())

grid = [
	list(map(int, input().split()))
	for _ in range(N)
]

steps = [
	[0 for _ in range(M)]
	for _ in range(N)
]

not_good_tomato = [(x, y) for x in range(N) for y in range(M) if grid[x][y] == 0]
good_tomato = [(x, y) for x in range(N) for y in range(M) if grid[x][y] == 1]

def in_range(x, y):
	return 0 <= x < N and 0 <= y < M

def bfs():
	q = deque(good_tomato[:])
	dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
	
	for x, y in good_tomato[:]:
		steps[x][y] = 1

	while q:
		x, y = q.popleft()
		step = steps[x][y]

		for dx, dy in zip(dxs, dys):
			nx, ny = x + dx, y + dy

			if in_range(nx, ny) and steps[nx][ny] == 0:
				if grid[nx][ny] == 0:
					steps[nx][ny] = step + 1
					q.append((nx, ny))
				elif grid[nx][ny] == -1:
					steps[nx][ny] = -1

bfs()


maxVal = 0
for i in range(N):
	for j in range(M):
		if steps[i][j] == 0 and (i, j) in not_good_tomato:
			print(-1)
			exit(0)
		maxVal = max(maxVal, steps[i][j])

if maxVal == 0:
	print(0)
else:
	print(maxVal - 1)
