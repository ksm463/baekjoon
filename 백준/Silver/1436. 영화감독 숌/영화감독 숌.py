input = int(input())

count = 0
number = 666
number_list = []

while count<10000:
    if '666' in str(number):
        number_list.append(number)
        count += 1
    
    number += 1

print(number_list[input-1])