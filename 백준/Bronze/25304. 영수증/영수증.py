X = int(input())
N = int(input())
list = [] 
c = 0
 
for i in range(N):
    a, b = map(int, input().split())
    list.append(a*b)

for i in range(N):
    c = c+list[i]

if X == c:
    print("Yes")
else:
    print("No")