import sys

N = int(sys.stdin.readline())

list_set = []
    
for _ in range(N):
    b, a = map(int, sys.stdin.readline().split())
    list_set.append([a, b])

list_set.sort()
    
for i in range(N):
    print(list_set[i][1], list_set[i][0])
