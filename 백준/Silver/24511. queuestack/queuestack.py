import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

DQ = deque()

for i in range(N):
    if (A[i] == 0):
        DQ.append(B[i])

for i in range(M):
    DQ.appendleft(C[i])
    print(DQ.pop(), end=' ')