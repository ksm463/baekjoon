import sys
input = sys.stdin.readline

while True:
    N = input().rstrip()
    
    if N == '.':
        break
    if not N:
        break
    
    stack = []
    is_valid = True

    for i in N:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                is_valid = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_valid = False
                break
    
    if is_valid and not stack:
        print('yes')
    else:
        print('no')


