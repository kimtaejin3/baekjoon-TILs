def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

ans = 0
check = []

def f(visited, numbers, selected, depth, n):
    global ans, check
    
    if depth == n:
        num = int(''.join(map(str, selected)))
        if num not in check:
            check.append(num)
            
            if is_prime(num):
                ans += 1
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            selected.append(numbers[i])
            visited[i] = True
            f(visited, numbers, selected, depth + 1, n)
            selected.pop()
            visited[i] = False
    
def solution(numbers):
    global ans
    numbers = list(map(int, numbers))
    for i in range(1, len(numbers) + 1):
        selected = []
        visited = [False for _ in range(len(numbers))]
        f(visited, numbers, selected, 0, i)

    return ans
