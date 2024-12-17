# https://www.acmicpc.net/problem/2504

S = input()
stack = []
tmp = 1  # 곱셈 계산을 위한 임시 변수
ans = 0  # 최종 결과값

for i in range(len(S)):
    if S[i] == '(':
        stack.append(S[i])
        tmp *= 2  # 여는 괄호 '('를 만나면 2를 곱함
    elif S[i] == '[':
        stack.append(S[i])
        tmp *= 3  # 여는 괄호 '['를 만나면 3을 곱함
    elif S[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if S[i-1] == '(':  # 직전 괄호가 여는 괄호면
            ans += tmp  # 현재까지의 곱셈값을 더함
        stack.pop()
        tmp //= 2  # 닫는 괄호를 만나면 2로 나눔
    else:  # ']' 인 경우
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if S[i-1] == '[':  # 직전 괄호가 여는 괄호면
            ans += tmp  # 현재까지의 곱셈값을 더함
        stack.pop()
        tmp //= 3  # 닫는 괄호를 만나면 3으로 나눔

if stack:  # 스택이 비어있지 않으면 올바르지 않은 괄호열
    print(0)
else:
    print(ans)
