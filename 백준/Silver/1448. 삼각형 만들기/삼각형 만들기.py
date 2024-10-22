n = int(input())

a = []

for _ in range(n):
    a.append(int(input()))

a = sorted(a)

left_index = n - 3
right_index = n

ans = -1
while left_index >= 0:
    s = a[left_index:right_index]

    if s[2] < s[0] + s[1]:
        ans = max(ans, sum(s))
    # print(s)

    left_index -= 1
    right_index = left_index + 3
    
print(ans)