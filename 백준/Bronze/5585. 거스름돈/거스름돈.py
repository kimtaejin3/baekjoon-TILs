n = int(input())

cnt = 0

n = 1000 - n

cnt += n // 500
n %= 500

# cnt: 1, n: 120

cnt += n // 100
n %= 100

# cnt: 2, n: 20

cnt += n // 50
n %= 50

# cnt: 2, n: 20

cnt += n // 10
n %= 10

# cnt: 4, n: 0

cnt += n // 5
n %= 5

print(cnt + n)

