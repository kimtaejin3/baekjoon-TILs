l, c = map(int, input().split())

a = input().split()
a.sort()

ans = []
s = []

moum = ['a', 'e', 'i', 'o', 'u']

def count_moum(s):
  count = 0
  
  for i in range(len(s)):
    if s[i] in moum:
      count += 1

  return count
      

def get_sequences(index, depth):
  
  if depth == l:
    str_s = ''.join(s)
    count = count_moum(str_s)

    if not (count < 1 or count > l-2):
      ans.append(''.join(s))
      
    return

  for i in range(index, c):
    s.append(a[i])
    get_sequences(i+1, depth+1)
    s.pop()
    
get_sequences(0,0)

for elem in ans:
  print(elem)
