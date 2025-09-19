import math

min = int(input())
max = int(input())

def find_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def prime_range(start, end):
    prime_list=[]
    if start > end:
        start, end = end, start
    
    for number in range(start, end+1):
        if find_prime(number):
            prime_list.append(number)
    
    return prime_list

primes = prime_range(min, max)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])

