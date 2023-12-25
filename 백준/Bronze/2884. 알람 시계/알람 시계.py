a, b = map(int, input().split())

if a == 0:
    a += 24
else: 
    a = a
c = 60*a + b - 45
d = c//60
if d == 24:
    d = 0
else: 
    d = d
e = c%60

print(d, e)