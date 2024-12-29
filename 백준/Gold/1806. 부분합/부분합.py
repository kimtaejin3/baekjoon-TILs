# https://www.acmicpc.net/problem/1806
# 1806번: 부분합
N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i-1] + arr[i]

right = 0
ans = N + 1

for left in range(1, N + 1):
    while right < N and psum[right] - psum[left - 1] < S:
        right += 1
    
    if right <= N and psum[right] - psum[left - 1] >= S:
        ans = min(ans, right - left + 1)

print(ans if ans <= N else 0)