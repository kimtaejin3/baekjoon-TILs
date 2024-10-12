N, K = map(int, input().split())

number = input()

stack = []

for i in range(len(number)):
    
    while stack and stack[-1] < number[i] and K > 0:
        stack.pop()
        K -= 1
    
    stack.append(number[i])

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))

