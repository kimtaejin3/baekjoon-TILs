from collections import deque

MAX_VAL = 100001
N, K = map(int, input().split())

visited = [False] * MAX_VAL
steps = [0] * MAX_VAL

def in_range(n):
    return 0 <= n < MAX_VAL

def find_min_dis():
    q = deque([N])
    visited[N] = True
    steps[N] = 0

    while q:
        num = q.popleft()
        
        if in_range(num-1) and not visited[num - 1]:
            visited[num - 1] = True
            steps[num - 1] = steps[num] + 1
            q.append((num - 1))
        
        if in_range(num+1) and not visited[num + 1]:
            visited[num + 1] = True
            steps[num + 1] = steps[num] + 1
            q.append((num + 1))
        
        if in_range(num * 2) and not visited[num * 2]:
            visited[num * 2] = True
            steps[num * 2] = steps[num] + 1
            q.append((num * 2))

find_min_dis()
print(steps[K])


    

