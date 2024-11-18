# https://www.acmicpc.net/problem/1717
# 유니온-파인드 알고리즘
# https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html

import sys
sys.setrecursionlimit(10**4)

MAX_SIZE = 1000000
root = [0] * (MAX_SIZE + 1)

for i in range(MAX_SIZE + 1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x

n, m = map(int, input().split())
ans = []
for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union(a, b)
    elif c == 1:
        if find(a) == find(b):
            ans.append('YES')
        else:
            ans.append('NO')

print('\n'.join(ans))

