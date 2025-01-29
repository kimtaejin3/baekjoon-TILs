from queue import PriorityQueue

N, M, X = map(int, input().split())

INF = int(1e12)
adj_list = [[] for _ in range(N + 1)]
dist_list = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b, t = map(int, input().split())
	adj_list[a].append([b, t])

def dijkstra(node):
	dist = [INF] * (N + 1)
	pq = PriorityQueue()
	pq.put([0, node])
	dist[node] = 0

	while not pq.empty():
		cur_dist, cur_node = pq.get()

		for adj_node, adj_dist in adj_list[cur_node]:
			temp_dist = cur_dist + adj_dist
			if temp_dist < dist[adj_node]:
				dist[adj_node] = temp_dist
				pq.put([temp_dist, adj_node])

	return dist

ans = -1
for town in range(1, N + 1):
	dist_list[town] = dijkstra(town)

for town in range(1, N + 1):
	temp = dist_list[town][X] + dist_list[X][town]
	ans = max(ans, temp)

print(ans)
