import sys
input = sys.stdin.readline

max = 246912
check_prime = [True] * (max + 1)
check_prime[0] = check_prime[1] = False


for i in range(2, int(max ** 0.5) + 1):
    if check_prime[i]:
        for j in range(i * i, max + 1, i):
            check_prime[j] = False

while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for i in range(N + 1, N * 2 + 1):
        prime_list = []
        if check_prime[i]:
            count += 1
    print(count)
