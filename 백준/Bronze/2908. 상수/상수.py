a, b = map(str, input().split())
r_a = int(a[::-1])
r_b = int(b[::-1])
if r_a >= r_b:
    c = r_a
else:
    c = r_b
print(c)