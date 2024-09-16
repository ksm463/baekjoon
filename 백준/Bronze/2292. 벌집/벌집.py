n = int(input())

hive_num = 1
line = 1

while n > hive_num:
    hive_num += line * 6
    line += 1

print(line)