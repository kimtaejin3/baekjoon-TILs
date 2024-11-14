import sys

N, H = map(int, input().split())
INT_MAX = sys.maxsize

def binary_search(arr, num):

    left = 0
    right = len(arr) - 1

    mid_val = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1

        if arr[mid] < num:
            mid_val = mid
    
    return mid_val

arr = []
for _ in range(N):
    arr.append(int(input()))

# 석순
stalagmite = []

#종유석
stalactite = []

for i in range(len(arr)):
    if i % 2 == 0:
        stalagmite.append(arr[i])
    else:
        stalactite.append(H - arr[i])

stalactite.sort()
stalagmite.sort()

# print(arr)
# print(stalactite)
# print(stalagmite)

# print(binary_search(stalagmite, 3.5))

h = 0.5

ans = sys.maxsize
cnt = -1

while h < H:
    v1 = len(stalagmite) - (binary_search(stalagmite, h) + 1)
    v2 = binary_search(stalactite, h) + 1
    
    if ans > v1 + v2:
        ans = v1 + v2
        cnt = 1
    elif ans == v1 + v2:
        cnt += 1

    h += 1

print(ans, cnt)