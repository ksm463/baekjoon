a, b, c = map(int, input().split())

d = (c-b)/(a-b)

if d == int(d):
    print(int(d))
else:
    print(int(d)+1)