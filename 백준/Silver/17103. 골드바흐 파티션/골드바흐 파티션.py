import sys
input = sys.stdin.readline

max = 1000000
check_prime = [True] * (max + 1)
check_prime[0] = check_prime[1] = False

T = int(input())

for i in range(2, int(max ** 0.5) + 1):
    if check_prime[i]:
        for j in range(i * i, max + 1, i):
            check_prime[j] = False

for _ in range(T):
    n = int(input())
    count = 0
    for a in range(2, n // 2 + 1):
        if check_prime[a]:
            b = n - a
            if check_prime[b]:
                count += 1
            
    print(count)
