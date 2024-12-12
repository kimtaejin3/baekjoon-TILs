t = int(input())
result = []
for _ in range(t):
    w = input()
    k = int(input())

    char_positions = {}

    for i, char in enumerate(w):
        if char not in char_positions:
            char_positions[char] = []
        
        char_positions[char].append(i)

    min_length = float('inf')
    max_length = -1

    for char, positions, in char_positions.items():
        if len(positions) < k:
            continue
        
        for i in range(len(positions) - k + 1):
            start = positions[i]
            end = positions[i + k - 1]
            length = end - start + 1

            min_length = min(min_length, length)
            max_length = max(max_length, length)
    
    if min_length == float('inf') or max_length == -1:
        result.append("-1")
    else:
        result.append(f"{min_length} {max_length}")


for elem in result:
    print(elem)





