import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    order = input().split()
    if order[0] == '1':
        stack.append(int(order[-1]))
    elif order[0] == '2':
        if stack:
            print(stack.pop(-1))
            continue
        print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if stack:
            print(0)
            continue
        print(1)
    elif order[0] == '5':
        if stack:
            print(stack[-1])
            continue
        print(-1)
