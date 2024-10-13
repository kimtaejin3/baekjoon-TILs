n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))
a.sort()

left_a = [elem for elem in a if elem < 0]
right_a = [elem for elem in a if elem > 0]

new_right_a = []
pack = 0
for i in range(len(right_a)-1, -1, -1):
    if pack == 0:
        new_right_a.append(right_a[i])
    
    pack += 1

    if pack == m:
        pack = 0

new_left_a = []
pack = 0
for i in range(0, len(left_a)):
    if pack == 0:
        new_left_a.append(left_a[i])
    
    pack += 1

    if pack == m:
        pack = 0

# print(left_a)
# print(right_a)

# print(new_left_a)
# print(new_right_a)

ans = 0

for i in range(len(new_right_a)):
    if i == 0:
        ans += new_right_a[i]
    else:
        ans += new_right_a[i] * 2

for i in range(len(new_left_a)):
    if i == 0:
        ans += abs(new_left_a[i]) 
    else:
        ans += abs(new_left_a[i]) * 2

if len(new_left_a) == 0:
    print(ans)
    exit(0)
elif len(new_right_a) == 0:
    print(ans)
    exit(0) 

if abs(new_left_a[0]) < new_right_a[0]:
    ans += abs(new_left_a[0])
else:
    ans += new_right_a[0]

print(ans)

