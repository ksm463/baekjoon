import sys
input = sys.stdin.readline
from collections import deque

N, C = map(int, input().split())
DQ = deque(range(1, N+1))
result = []

while DQ:
    DQ.rotate(-(C-1))
    result.append(DQ.popleft())

print(f"<{', '.join(map(str, result))}>")
