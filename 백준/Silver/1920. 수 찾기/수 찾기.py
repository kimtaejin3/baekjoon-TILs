def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    
    return 0


N = int(input())
A = list(map(int, input().split()))
M = int(input())

A.sort()
nums = list(map(int, input().split()))

for num in nums:
    print(binary_search(A, num))



