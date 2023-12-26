a, b, c = map(int, input().split())
d = [a, b, c]

if a==b==c:
    e = a*1000 + 10000
elif a==b:
    e = a*100 + 1000
elif b==c:
    e = b*100 + 1000
elif a==c:
    e = a*100 + 1000
else:
    e = max(d)*100
print(e)