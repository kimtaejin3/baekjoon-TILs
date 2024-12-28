N, M = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
for left in range(N):
    cur_sum = 0
    for right in range(left, N):
        cur_sum += A[right]
        if cur_sum == M:
            ans += 1

print(ans)

