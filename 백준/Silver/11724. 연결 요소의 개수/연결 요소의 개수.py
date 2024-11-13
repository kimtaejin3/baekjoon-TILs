from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


def bfs(v):
    q = deque([v])

    while q:
        popped = q.popleft()

        for cv in graph[popped]:
            if not visited[cv]:
                visited[cv] = True
                q.append(cv)


cnt = 0
for i in range(1, N+1):

    if not visited[i]:
        visited[i] = True
        cnt += 1
        bfs(i)

print(cnt)
