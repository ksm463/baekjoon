import sys
import math
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    L = int(input())
    num_list.append(L)

def find_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for start_num in num_list:
    num = start_num
    while True:
        if find_prime(num):
            print(num)
            break
        num += 1
