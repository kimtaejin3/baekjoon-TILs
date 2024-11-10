t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    s = input()

    arr = []

    if len(s) == 2:
        arr = []
    else:
        arr = list(map(int, s[1:len(s)-1].split(",")))

    error = False
    reverse = False

    for cmd in p:
        if cmd == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        elif cmd == 'D':
            if len(arr) == 0:
                error = True
                break
            if not reverse:
                arr.pop(0)
            else:
                arr.pop()

    if error:
        print('error')
    else:
        if reverse:
            print('['+','.join(map(str,arr[::-1]))+']')
        else:
            print('['+','.join(map(str,arr))+']')