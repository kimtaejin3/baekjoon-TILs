N, M = map(int, input().split())

arr = list(map(int, input().split()))

def get_woods(num):
    sum = 0

    for i in range(len(arr)):
        if num < arr[i]:
            sum += arr[i] - num
    
    return sum

def binary_search():
    left = 0
    right = 1000000000
    result = 0

    while left <= right:
        
        mid = (left + right) // 2
        mid_val = get_woods(mid)

        if mid_val >= M:
            result = mid
            left = mid + 1  
        else:
            right = mid - 1

    return result

ans = binary_search()
print(ans)



