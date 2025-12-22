import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    order = int(input())
    if order == 0:
        stack.pop(-1)
    else:
        stack.append(int(order))

print(sum(stack))
