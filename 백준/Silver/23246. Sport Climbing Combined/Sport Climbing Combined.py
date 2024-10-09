n = int(input())

a = []
for _ in range(n):
  b, p, q, r = tuple(map(int,input().split()))
  a.append((b, p, q, r))

a.sort(key = lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3] , x[0]))

for i in range(3):
  print(a[i][0], end=' ')
