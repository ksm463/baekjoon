import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
DQ = deque(enumerate(map(int, input().split())))
result = []

while DQ:
    idx, num = DQ.popleft()
    result.append(idx + 1)
    
    if num > 0:
        DQ.rotate(-(num - 1))
    elif num < 0:
        DQ.rotate(-num)

print(' '.join(map(str, result)))