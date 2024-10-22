import sys
input = sys.stdin.readline
n = int(input())

a = []

for _ in range(n):
    a.append(int(input()))

a = sorted(a, reverse=True)

for i in range(0, len(a)):
    if sum(a[i+1:i+3]) > a[i]:
        print(sum(a[i:i+3]))
        break

else:
    print(-1)
