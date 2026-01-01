import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
DQ = deque()

for _ in range(N):
    order = input().split()
    O = int(order[0])
    
    if O == 1:
        DQ.appendleft(order[1])
    
    elif O == 2:
        DQ.append(order[1])
    
    elif O == 3:
        if DQ:
            print(DQ[0])
            DQ.popleft()
        else:
            print(-1)
    
    elif O == 4:
        if DQ:
            print(DQ[-1])
            DQ.pop()
        
        else:
            print(-1)
    
    elif O == 5:
        print(len(DQ))
    
    elif O == 6:
        if DQ:
            print(0)
        else:
            print(1)
    
    elif O ==7:
        if DQ:
            print(DQ[0])
        else:
            print(-1)
    
    elif O ==8:
        if DQ:
            print(DQ[-1])
        else:
            print(-1)


