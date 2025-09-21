a_x, a_y = map(int, input().split())
b_x, b_y = map(int, input().split())
c_x, c_y = map(int, input().split())

def find_unique(n1, n2, n3):
    if n1 == n2:
        return n3
    elif n1 == n3:
        return n2
    else:
        return n1

x_unique = find_unique(a_x, b_x, c_x)
y_unique = find_unique(a_y, b_y, c_y)

print(x_unique, y_unique)