import sys
input = lambda: sys.stdin.readline().rstrip()
from queue import PriorityQueue

INF = int(1e12)

V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V + 1)]

dist = [INF] * (V + 1)
pq = PriorityQueue()
pq.put((0, K))
dist[K] = 0

for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))

while not pq.empty():
	cur_dist, cur_node = pq.get()

	for adj_node, adj_dist in graph[cur_node]:
		temp_dist = cur_dist + adj_dist

		if temp_dist < dist[adj_node]:
			pq.put((temp_dist, adj_node))
			dist[adj_node] = temp_dist


for i in range(1, len(dist)):
	if dist[i] == INF:
		print('INF')
		continue
	print(dist[i])
