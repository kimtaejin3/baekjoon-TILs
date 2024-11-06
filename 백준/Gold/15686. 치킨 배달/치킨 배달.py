# https://www.acmicpc.net/problem/15686\
import sys

INT_MAX = sys.maxsize

N, M = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

chicken_shop = [
    (i, j)
    for i in range(N)
    for j in range(N)
    if grid[i][j] == 2
]

houses = [
    (i, j)
    for i in range(N)
    for j in range(N)
    if grid[i][j] == 1
]

selected_chicken_shop = list()

def calc():
    sum_of_min_dis = 0

    for house in houses:
        min_val = INT_MAX
        for chicken_shop in selected_chicken_shop:
            hx, hy = house
            cx, cy = chicken_shop

            min_val = min(abs(hx - cx) + abs(hy - cy), min_val)
        sum_of_min_dis += min_val

    return sum_of_min_dis

ans = INT_MAX

def choose(lev, cnt, num):
    global ans 
    
    if cnt == num:
        ans = min(ans, calc())
        return

    if lev == len(chicken_shop):
        return
    
    selected_chicken_shop.append(chicken_shop[lev])
    choose(lev + 1, cnt + 1, num)
    selected_chicken_shop.pop()

    choose(lev + 1, cnt, num)

def simulate():
    global selected_chicken_shop

    for i in range(1, M + 1):
        selected_chicken_shop = list()
        choose(0, 0, i)

simulate()

print(ans)

