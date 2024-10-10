def search(lev):
  global N, S, arr, choose, ans

  if lev == N:
    if choose and sum(choose) == S:
      ans += 1
    return

  choose.append(arr[lev])
  search(lev + 1)
  choose.pop()

  search(lev + 1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
choose = []
ans = 0

search(0)

print(ans)