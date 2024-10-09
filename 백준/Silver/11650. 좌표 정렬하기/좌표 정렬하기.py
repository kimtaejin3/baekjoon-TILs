n = int(input())

a = []
for _ in range(n):
  x,y = tuple(map(int,input().split()))
  a.append((x,y))

a.sort()

for elem in a:
  print(' '.join(map(str,elem)))
