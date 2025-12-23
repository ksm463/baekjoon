import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    stack = []
    order = input()
    for j in order:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
