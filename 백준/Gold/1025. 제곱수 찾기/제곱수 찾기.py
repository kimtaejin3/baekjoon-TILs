import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
answer = -1

def is_perfect(s):
    s = int(s)
    return int(s ** 0.5) ** 2 == s

for i in range(N):
    for j in range(M):
        for row_d in range(-N, N):
            for col_d in range(-M, M):
                s = ""

                x, y = i, j

                if row_d == 0 and col_d == 0:
                    continue

                while 0 <= x < N and 0 <= y < M:
                    s += board[x][y]
                    if is_perfect(s):
                        answer = max(answer, int(s))
                    
                    x += row_d
                    y += col_d

print(answer)

