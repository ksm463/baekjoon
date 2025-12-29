import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
DQ = deque()

for _ in range(N):
    order  = input().split()
    
    if order[0] == 'push':
        DQ.append(int(order[1]))
    
    if order[0] == 'pop':
        if DQ:
            print(DQ.popleft())
        else:
            print(-1)
    
    if order[0] == 'size':
        print(len(DQ))
    
    if order[0] == 'empty':
        if DQ:
            print(0)
        else:
            print(1)
    
    if order[0] == 'front':
        if DQ:
            print(DQ[0])
        else:
            print(-1)
    
    if order[0] == 'back':
        if DQ:
            print(DQ[-1])
        else:
            print(-1)
