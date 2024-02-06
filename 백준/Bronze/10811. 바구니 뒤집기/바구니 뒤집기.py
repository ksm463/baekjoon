n, m = map(int, input().split())
bag = [i for i in range(1, n+1)]
a = 0
for x in range(m):
  i, j = map(int, input().split())
  a = bag[i-1:j]
  a.reverse()
  bag[i-1:j] = a

for x in range(n):
  print(bag[x], end=" ")