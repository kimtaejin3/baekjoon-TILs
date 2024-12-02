from collections import deque

N, M = map(int, input().split())

ladders = {}
snakes = {}

visited = [
    False
    for _ in range(101)
]
step = [
    0
    for _ in range(101)
]

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v


def bfs():
    q = deque([1])
    visited[1] = True
    step[1] = 0

    while q:
        poppedEl = q.popleft()

        for i in range(1, 7):

            if poppedEl + i in ladders:
                newEl = ladders[poppedEl + i]
            elif poppedEl + i in snakes:
                newEl = snakes[poppedEl + i]
            else:
                if poppedEl + i <= 100:
                    newEl = poppedEl + i
            
            if newEl <= 100 and not visited[newEl]:
                visited[newEl] = True
                step[newEl] = step[poppedEl] + 1
                q.append(newEl)

bfs()
print(step[100])



