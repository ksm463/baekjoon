import sys
input = sys.stdin.readline

N = int(input())
target = {'ChongChong'}

for _ in range(N):
    a, b = input().rstrip().split()
    if a in target:
        target.add(b)
    if b in target:
        target.add(a)

print(len(target))