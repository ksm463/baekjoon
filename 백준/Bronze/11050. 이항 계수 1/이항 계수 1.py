import sys
input = sys.stdin.readline

N, K = map(int, input().split())

n_fac = 1
for i in range(K):
    n_fac *= (N - i)

k_fac = 1
for i in range(1, K+1):
    k_fac *= i

print(n_fac // k_fac)