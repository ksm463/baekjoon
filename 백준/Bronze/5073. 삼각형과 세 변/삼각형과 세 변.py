while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif a == b == c:
        print("Equilateral")
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Invalid")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        print("Isosceles")
    elif a != b and a != c and b != c:
        print("Scalene")
