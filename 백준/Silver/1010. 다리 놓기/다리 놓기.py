import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    m_minus_n_fac = 1
    for i in range(M - N):
        m_minus_n_fac *= i+1

    n_fac = 1
    for i in range(N):
        n_fac *= i+1

    m_fac = 1
    for i in range(M):
        m_fac *= i+1

    print(m_fac // (n_fac * m_minus_n_fac))