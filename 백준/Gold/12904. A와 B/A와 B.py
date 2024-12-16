# https://www.acmicpc.net/problem/12904
S = input()
T = input()
r = ''
ans = 0

while T != '':
    if T[-1] == 'A':
        T = T[0:len(T)-1]
    elif T[-1] == 'B':
        T = T[0:len(T)-1]
        T = T[::-1]
    if T == S:
        ans = 1


print(ans)
