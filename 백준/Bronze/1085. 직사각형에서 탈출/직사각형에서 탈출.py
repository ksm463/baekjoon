x, y, w, h = map(int, input().split())

short_list = [x, y, w-x, h-y]

print(min(short_list))