import sys

lines = int(sys.stdin.readline())

# 리스트를 미리 만들어 메모리를 할당해 놓음
numbers = [0] * 10001

for _ in range(lines):
    num = int(sys.stdin.readline())
    numbers[num] += 1

for n in range(1, 10001):
    if numbers[n] > 0:
        for _ in range(numbers[n]):
            print(n)
