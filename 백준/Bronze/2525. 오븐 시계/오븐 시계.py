a, b = map(int, input().split())
f = int(input())

c = 60*a + b + f
d = c//60
if d >= 24:
    d = d -24
else: 
    d = d
e = c%60

print(d, e)