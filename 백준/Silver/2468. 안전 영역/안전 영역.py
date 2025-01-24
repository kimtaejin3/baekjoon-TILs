from collections import deque

N = int(input())

grid = [
	list(map(int, input().split()))
	for _ in range(N)
]

visited = [
	[False for _ in range(N)]
	for _ in range(N)
]

def init_visited():
	for i in range(N):
		for j in range(N):
			visited[i][j] = False

def in_range(x, y):
	return 0 <= x < N and 0 <= y < N

def bfs(x, y, k):
	dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
	
	q = deque([(x, y)])

	while q:
		x, y = q.popleft()
		for dx, dy in zip(dxs, dys):
			
			nx, ny = x + dx, y + dy

			if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > k:
				visited[nx][ny] = True
				q.append((nx, ny))


ans = 0
for k in range(101):
	init_visited()
	cnt = 0
	for x in range(N):
		for y in range(N):
			if grid[x][y] > k and not visited[x][y]:
				cnt += 1
				visited[x][y] = True
				bfs(x, y, k)
	ans = max(cnt, ans)

print(ans)

