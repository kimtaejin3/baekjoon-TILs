def make(lev):
  global n, words, choose, ans, cnt
  #base case
  if lev == n:
    ans += 1
    return

  #recursive case
  for word in words:
    if cnt[word] == 0:
      continue
    if (not choose) or choose[-1] != word:
      choose.append(word)
      cnt[word] -= 1
      make(lev + 1)
      cnt[word] += 1
      choose.pop()


s = input()
n = len(s)
cnt = dict()
ans = 0

words = set(s)
choose = []

for word in list(s):
  if word not in cnt:
    cnt[word] = 1
  else:
    cnt[word] += 1

make(0)

print(ans)

