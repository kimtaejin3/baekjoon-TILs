n, d, k, c = map(int, input().split())
rail = []

for _ in range(n):
    rail.append(int(input()))

ans = -1

for i in range(n):
    window = []
    for j in range(k):
        if i + j < n:
            window.append(rail[i + j])
        else:
            window.append(rail[i + j - n])

    window.append(c)
    set_window = set(window)

    ans = max(ans, len(set_window))


print(ans)
