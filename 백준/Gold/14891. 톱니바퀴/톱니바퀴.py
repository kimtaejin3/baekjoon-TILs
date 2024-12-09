# https://www.acmicpc.net/problem/14891
arr = [
    list(map(int, input().strip()))
    for _ in range(4)
]

visited = [False for _ in range(4)]

K = int(input())

def roll_left(n):
    temp = arr[n][0]

    for i in range(1, 8):
        arr[n][i - 1] = arr[n][i]
    
    arr[n][7] = temp

def roll_right(n):
    temp = arr[n][7]
    
    for i in range(7, 0, -1):
        arr[n][i] = arr[n][i - 1]
    
    arr[n][0] = temp

def f(n, d):
    if n < 0 or n > 3:
        return
    
    up_n, down_n = n - 1, n + 1

    if up_n >= 0 and arr[up_n][2] != arr[n][6] and not visited[up_n]:
        visited[up_n] = True
        f(up_n, d * (-1))
    
    if down_n < 4 and arr[down_n][6] != arr[n][2] and not visited[down_n]:
        visited[down_n] = True
        f(down_n, d * (-1))

    if d == 1:
        roll_right(n)
    elif d == -1:
        roll_left(n)
    
   



for _ in range(K):
    n, d = map(int, input().split())
    for i in range(4):
        visited[i] = False
    n -= 1
    visited[n] = True
    f(n, d)



ans = 0

for i in range(4):
    if arr[i][0] == 1:
        ans += 2 ** (i)
print(ans)
