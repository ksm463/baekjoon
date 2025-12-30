import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
DQ = deque()

for i in range(N):
    j = i + 1
    DQ.append(j)

while True:
    if len(DQ) == 1:
        print(DQ[0])
        break
    
    DQ.popleft()
    DQ.rotate(-1)

    