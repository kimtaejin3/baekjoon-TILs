# https://www.acmicpc.net/problem/2110

def is_possible(k):
    global N, C

    bef_idx = 0
    cnt = 1

    for idx in range(1, N):
        if x[idx] - x[bef_idx] >= k:
            bef_idx = idx
            cnt += 1

    return cnt >= C

x = []
N, C = map(int, input().split())

for _ in range(N):
    x.append(int(input()))

x.sort()

# parametric search
cur = -1
step = int(1e9) + 1

while step != 0:
    while (cur + step <= int(1e9)) and is_possible(cur + step):
        cur += step 
    step //= 2

print(cur)

