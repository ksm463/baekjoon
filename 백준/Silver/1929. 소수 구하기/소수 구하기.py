import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def find_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(N, M + 1):
    if find_prime(i):
        print(i)
    else:
        pass