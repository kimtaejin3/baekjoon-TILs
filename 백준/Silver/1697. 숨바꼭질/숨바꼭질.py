from collections import deque

N, K = map(int, input().split())
MAX_NUM = 100000

arr = [-1 for _ in range(MAX_NUM + 1)]

def bfs(x):
	q = deque([x])
	arr[x] = 0

	while q:
		popped = q.popleft()
		
		if popped - 1 >= 0 and  arr[popped - 1] == -1:
			arr[popped - 1] = arr[popped] + 1
			q.append(popped - 1)
		
		if popped + 1 < MAX_NUM + 1 and arr[popped + 1] == -1:
			arr[popped + 1] = arr[popped] + 1
			q.append(popped + 1)
		
		if popped * 2 < MAX_NUM + 1 and  arr[popped * 2] == -1:
			arr[popped * 2] = arr[popped] + 1
			q.append(popped * 2)
		    
bfs(N)

print(arr[K])
