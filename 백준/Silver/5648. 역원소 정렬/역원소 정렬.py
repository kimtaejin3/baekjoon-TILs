import sys
def input(): return sys.stdin.read()

N, *numbers = input().split()

for i in range(int(N)): numbers[i] = int(numbers[i][::-1])

numbers.sort()

for i in range(int(N)):print(numbers[i])
