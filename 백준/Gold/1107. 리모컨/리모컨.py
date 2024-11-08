# https://www.acmicpc.net/problem/1107

import sys

INT_MAX = sys.maxsize

N = int(input())
M = int(input())

size_N = len(str(N))
arr = []
if M > 0:
    arr = list(map(int, input().split()))
new_arr = [i for i in range(10) if i not in arr]

choose = []
cnt = 0
min_gap = INT_MAX
min_val = -1

cnt = 0

def select(lev, n):
    global cnt, min_gap, min_val

    cnt += 1

    if lev == n:
        num = int(''.join(map(str, choose)))
        # print(num)
        if abs(num - N) < min_gap:
            min_gap = abs(num - N)
            min_val = num
        return

    for i in range(len(new_arr)):

        choose.append(new_arr[i])
        select(lev + 1, n)
        choose.pop()

def select_all():
    if size_N == 1:
        select(0, 1)
        select(0, 2)
    elif size_N > 1:
        for i in range(size_N - 1, size_N + 2):
            select(0, i)

select_all()

min_str = str(min_val)
ans = len(min_str) + min_gap

if ans > abs(N - 100):
    print(abs(N-100))
else:
    print(ans)

# print(cnt)