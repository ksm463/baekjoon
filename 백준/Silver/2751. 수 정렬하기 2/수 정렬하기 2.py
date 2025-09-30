import sys

lines = int(sys.stdin.readline())

numbers = []

for _ in range(lines):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

for n in numbers:
    print(n)