num = int(input())

result = 0

for i in range(1, num - 1):
    set_digit = list(map(int, str(i)))
    digit_sum = i + sum(set_digit)
    if digit_sum == num:
        result = i
        break

print(result)
