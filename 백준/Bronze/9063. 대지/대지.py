num = int(input())

x_list = []
y_list = []

if num <= 1:
    print(0)
else:
    for i in range(1, num+1):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    x_line = max(x_list) - min(x_list)
    y_line = max(y_list) - min(y_list)

    print(x_line * y_line)