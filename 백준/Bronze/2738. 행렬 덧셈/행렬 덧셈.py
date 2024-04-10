a, b = [], []
N, M = map(int, input().split())

for i in range(N):
    i = list(map(int, input().split()))
    a.append(i)

for i in range(N):
    i = list(map(int, input().split()))
    b.append(i)
    
for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end = ' ')
    print()