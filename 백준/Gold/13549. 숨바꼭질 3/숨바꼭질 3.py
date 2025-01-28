import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)
Index = 100001
N, K = map(int, input().split())

dist = [INF] * (Index)

pq = PriorityQueue()
dist[N] = 0
pq.put([0, N])

adj_list = [[] for _ in range(Index)]

for i in range(Index):
	if i - 1 >= 0:
		adj_list[i].append([i - 1, 1])
	if i + 1 < Index:
		adj_list[i].append([i + 1, 1])
	if i * 2 < Index:
		adj_list[i].append([i * 2, 0])

while not pq.empty():
	cur_dist, cur_node = pq.get()
	for adj_node, adj_dist in adj_list[cur_node]:
		temp_dist = cur_dist + adj_dist
		if temp_dist < dist[adj_node]:
			dist[adj_node] = temp_dist
			pq.put([temp_dist, adj_node])
	
print(dist[K])


