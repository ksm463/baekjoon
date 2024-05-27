N = int(input())
white = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range (x, x+10):
        for j in range (y, y+10):
            white[i][j] = 1

result = 0
for a in range(100):
    result += white[a].count(1)

print(result)