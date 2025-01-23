from collections import deque

def get_diff_cnt(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    
    return cnt

def bfs(v, words, target):
    visited = {}
    
    for word in words:
        visited[word] = False
    
    q = deque([(v, 0)])
    res = 0
    
    while q:
        popped_v, cnt = q.popleft()
        for word in words:
            if get_diff_cnt(popped_v, word) == 1:
                if not visited[word]:
                    q.append((word, cnt + 1))
                    visited[word] = True
                continue
            
            if get_diff_cnt(popped_v, target) == 0:
                res = cnt
    
    return res

def solution(begin, target, words):
    answer = bfs(begin, words, target)
    return answer