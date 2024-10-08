n = int(input())

choose = []
check = [False] * (n + 1)

def permutation(level):

  if level == n:
    print(' '.join(map(str,choose)))

  else:
    for i in range(1, n+1):
      if check[i]:
        continue

      choose.append(i)
      check[i] = True
      
      permutation(level + 1)

      check[i] = False
      choose.pop()

permutation(0)
