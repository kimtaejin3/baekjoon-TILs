def solution(progresses, speeds):
    answer = []
    a = []
    stack = []
    count = []
    
    for progress, speed in zip(progresses, speeds):
        val = (100 - progress) // speed
        
        if (100 - progress) % speed != 0:
            val += 1
        
        a.append(val)
    
    cnt = 0
    
    for elem in a:
        if not stack:
            stack.append(elem)
            continue
        if stack[-1] < elem:
            count.append(cnt + 1)
            cnt = 0
            stack.append(elem)
        else:
            cnt += 1
    
    
    count.append(cnt + 1)
    
    print(a)
    print(stack)
    print(count)
    
    return count


