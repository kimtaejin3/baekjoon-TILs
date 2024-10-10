n = int(input())

def check(str1, str2):
  strike, ball = 0, 0
  
  for i in range(3):
    if str1[i] == str2[i]:
      strike += 1
    else:
      if str1[i] in list(str2):
        ball += 1
  # print(str1, str2, strike, ball)
  return (strike, ball)
  

a = []
for _ in range(n):
  num, strike, ball = input().split()
  strike, ball = int(strike), int(ball)

  a.append((num, strike, ball))
ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    for k in range(1,10):
      if i == j or j == k or i == k:
        continue
      
      is_possible = True

      for l in range(n):
        num, strike, ball = a[l]
        strike2, ball2 = check(str(i * 100 + j * 10 + k), num)

        if strike != strike2 or ball != ball2:
          is_possible = False

      if is_possible:
        ans += 1

print(ans)
        
        
