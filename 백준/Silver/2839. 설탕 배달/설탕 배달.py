input = int(input())

def calculate_div(num):
    div_five = input // 5
    
    for count_five in range(div_five, -1, -1):
        remain = num - (5 * count_five)
        
        if remain >= 0 and remain % 3 == 0:
            div_three = remain // 3
            return count_five + div_three
        
    return -1

div_total = calculate_div(input)

print(div_total)
