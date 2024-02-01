N, M = map(int, input().split())
bag = [i for i in range(1, N+1)]
set = 0

for i in range(M):
    i, j = map(int, input().split())
    set = bag[i-1]
    bag[i-1] = bag[j-1]
    bag[j-1] = set

for i in range(N):
    print(bag[i], end=' ')