from collections import deque

def bfs(house, locations, festival):
    # BFS를 위한 큐와 방문 처리 집합
    queue = deque([house])
    visited = set([house])

    while queue:
        x, y = queue.popleft()

        # 페스티벌 도착 시 종료
        if (x, y) == festival:
            print("happy")
            return
        
        # 모든 위치를 순회하며 1000m 이내인지 확인
        for nx, ny in locations:
            if (nx, ny) not in visited and abs(nx - x) + abs(ny - y) <= 1000:
                visited.add((nx, ny))
                queue.append((nx, ny))

    # 페스티벌에 도달하지 못했을 경우
    print("sad")


# 입력 처리
t = int(input())  # 테스트 케이스 수

for _ in range(t):
    n = int(input())  # 편의점 개수

    # 좌표 입력
    house = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))

    # BFS 실행
    bfs(house, stores + [festival], festival)
