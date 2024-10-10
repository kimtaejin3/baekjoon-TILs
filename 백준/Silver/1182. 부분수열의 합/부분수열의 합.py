n, s = map(int, input().split())

a = list(map(int, input().split()))

choose = []

ans = 0

def sequence(index, level, length):
  global ans
  
  if level == length:
    if sum(choose) == s:
      ans += 1
    return

  for i in range(index, n):
    choose.append(a[i])
    sequence(i + 1, level + 1, length)
    choose.pop()


for i in range(n):
  sequence(0,0,i+1)

print(ans)
