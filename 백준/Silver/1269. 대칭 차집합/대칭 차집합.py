import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_set = set(map(int, input().split()))
m_set = set(map(int, input().split()))
    
sym_n = n_set - m_set
sym_m = m_set - n_set

print(len(sym_n) + len(sym_m))