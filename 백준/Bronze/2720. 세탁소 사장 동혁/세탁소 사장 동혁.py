a = int(input())

for _ in range(a):
    b = int(input())
    c = []
    for i in [25, 10, 5, 1]:
        c.append(b//i)
        b = b%i
    
    print(*c)