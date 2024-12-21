# https://www.acmicpc.net/problem/13397

def can_divide(arr, m, max_diff):
    count = 1
    current_min = arr[0]
    current_max = arr[0]

    for num in arr:
        if num < current_min:
            current_min = num
        if num > current_max:
            current_max = num

        if current_max - current_min > max_diff:
            count += 1
            current_min = num
            current_max = num

    return count <= m

def solve(n, m, arr):
    left = 0
    right = max(arr) - min(arr)

    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_divide(arr, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(n, m, arr))

