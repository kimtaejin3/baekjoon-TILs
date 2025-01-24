from collections import deque

def check(elem, arr):
    for a in arr:
        if elem[0] < a[0]:
            return True
        
    return False
        
def solution(priorities, location):
    answer = 0
    arr = []
    result = []
    ans = -1
    
    for i, priority in enumerate(priorities):
        arr.append((priority, i))
    
    q = deque(arr[:])
    
    while q:
        elem = q.popleft()
        
        if check(elem, list(q)[0:]):
            q.append(elem)
        else:
            # execute
            result.append(elem)
    
    for i, r in enumerate(result):
        p, n = r
        
        if n == location:
            ans = i + 1
        
    return ans