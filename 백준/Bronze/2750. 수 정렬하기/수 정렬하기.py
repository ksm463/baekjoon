lines = int(input())

numbers = []

for _ in range(lines):
    num = int(input())
    numbers.append(num)

numbers.sort()

for n in numbers:
    print(n)