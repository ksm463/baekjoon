num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
if line % 2 == 0:
    s = num
    m = line - num + 1

elif line % 2 == 1:
    s = line - num + 1
    m = num

print(f'{s}/{m}')