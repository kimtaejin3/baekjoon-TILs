n = int(input())

meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key = lambda x:(x[1], x[0]))

cnt = 1
last_end = meetings[0][1]

for i in range(1, len(meetings)):
    s, e = meetings[i]

    if s >= last_end:
        cnt += 1
        last_end = e

print(cnt)



