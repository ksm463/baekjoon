input_list = []

for i in range(5):
    num = int(input())
    input_list.append(num)
    input_list.sort()
    
sum_list = sum(input_list)
avg = sum_list / 5
mid = input_list[2]

print(int(avg))
print(mid)