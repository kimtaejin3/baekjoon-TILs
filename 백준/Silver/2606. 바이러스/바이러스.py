n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt = 0

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def dfs(v):
	global cnt
	visited[v] = True
	cnt += 1

	for c_v in graph[v]:
		if not visited[c_v]:
			dfs(c_v)

dfs(1)
print(cnt - 1)
