# 프로그래머스 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=python3
import sys
sys.setrecursionlimit(10**9)

def init_coordinates(rectangle):
    coordinates = []
    for elem in rectangle:
        x1, y1, x2, y2 = elem

        coordinates.append((x1,y1))
        coordinates.append((x2,y2))
        coordinates.append((x1,y2))
        coordinates.append((x2,y1))
    return coordinates

def get_intersect_coordinates(rectangle):
    ans = []
    a = [
        [0 for _ in range(51)]
        for _ in range(51)
    ]
    
    for elem in rectangle:
        x1, y1, x2, y2 = elem
        
        for i in range(x1, x2 + 1):
            a[i][y1] += 1
            a[i][y2] += 1
        
        for i in range(y1, y2 + 1):
            a[x1][i] += 1
            a[x2][i] += 1
        
        a[x1][y1] -= 1
        a[x2][y2] -= 1
        a[x1][y2] -= 1
        a[x2][y1] -= 1
    
    cnt = 0
    for row in a:
        for elem in row:
            if elem > 1:
                cnt += 1

    for i in range(51):
        for j in range(51):
            if a[i][j] > 1:
                ans.append((i,j))
    
    return ans

def remove_unnessesary_coordinates(coordinates, rectangle):
    
    new_coordinates = []

    for coordinate in coordinates:
        is_unnessesary = False
        x, y = coordinate

        for elem in rectangle:
            x1, y1, x2, y2 = elem

            if x1 < x < x2 and y1 < y < y2:
                is_unnessesary = True
        
        if not is_unnessesary:
            new_coordinates.append(coordinate)

    return new_coordinates

def can_go(x1, y1, x2, y2, rectangle):
    is_possible = True

    if x1 == x2 and y1 == y2:
        return True
   
    for elem in rectangle:
        rx1, ry1, rx2, ry2 = elem

        if x1 == x2:
            if rx1 < x1 < rx2 and ((y1 <= ry1 and y2 >= ry2 and y1 < y2) or (y1 >= ry2 and y2 <= ry1 and y1 > y2)):
                is_possible = False
        elif y1 == y2:
            if ry1 < y1 < ry2 and ((x1 <= rx1 and x2 >= rx2 and  x1 < x2) or (x1 >= rx2 and x2 <= rx1 and x1 > x2)):
                is_possible = False

   
    return is_possible


# print(can_go(1,4,6,4,[[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]]))

ans = sys.maxsize
temp_ans = -1 

def operate(coordinates, character, item, rectangle, dist, direction, lev):
    global ans

    cur_x, cur_y = character
    dest_x, dest_y = item

    # print(cur_x, cur_y)

    #base case
    if (cur_x == dest_x or cur_y == dest_y) and can_go(cur_x, cur_y, dest_x, dest_y, rectangle):
        # print('right', dist)
        if cur_x == dest_x:
            # print(dist + abs(cur_y - dest_y))
            ans = min(ans, dist + abs(cur_y - dest_y))
        else:
            # print(dist + abs(cur_x - dest_x))
            ans = min(ans, dist + abs(cur_x - dest_x))

        return
    
    #recursive case
    for coordinate in coordinates:
        next_x, next_y = coordinate

       
        if (next_x == cur_x and next_y == cur_y):
            continue
        
        if (direction == 'b' and next_x == cur_x) or (direction == 'c' and next_y == cur_y):
            if can_go(cur_x, cur_y, next_x, next_y, rectangle):
                added_dist = 0
                
                sub_direction = 'a'

                if cur_x == next_x:
                    added_dist = abs(cur_y - next_y)
                    sub_direction = 'c'
                elif cur_y == next_y:
                    added_dist = abs(cur_x - next_x)
                    sub_direction = 'b'
                
                operate(coordinates, (next_x, next_y), item, rectangle, dist+added_dist, sub_direction, lev + 1)

def solution(rectangle, characterX, characterY, itemX, itemY):
    coordinates = init_coordinates(rectangle)
    interseting_coordinates = get_intersect_coordinates(rectangle)
    
    for coordinate in interseting_coordinates:
        coordinates.append(coordinate)
    
    new_coordinates = remove_unnessesary_coordinates(coordinates, rectangle)
    new_coordinates.sort()
    
    start_coordinates = []
    for elem in new_coordinates:
        x, y = elem
        if characterX != x and characterY != y:
            start_coordinates.append(elem)
        else:
            if (characterX == x or characterY == y) and not can_go(characterX,characterY,x,y,rectangle):
                start_coordinates.append(elem)

    for coordinate in new_coordinates:
        cx, cy = coordinate
        if characterX == cx or characterY == cy:
            # 밑에 디스트만 채우기
            init_dist = 0
            d = ''
            if characterX == cx:
                init_dist = abs(characterY - cy)
                d = 'c'
            elif characterY == cy:
                init_dist = abs(characterX - cx)
                d = 'b'
            
            if can_go(characterX, characterY, cx, cy, rectangle):
                # print(start_coordinates)
                operate(start_coordinates, (cx, cy), (itemX, itemY), rectangle, init_dist, d, 0)
                # print('== == ==')

    return ans

# solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
# solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],1, 3, 7, 8)
# a = solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)
# a = solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
# print(a)