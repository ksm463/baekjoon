a, b, c = map(int, input().split())

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a

while a >= b + c:
    a -= 1

print(a + b + c)