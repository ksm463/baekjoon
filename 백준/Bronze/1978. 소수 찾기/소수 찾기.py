import math

number = int(input())
number_list = list(map(int, input().split()))

def find_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

prime_count = 0

for num in number_list:
    if find_prime(num):
        prime_count += 1

print(prime_count)