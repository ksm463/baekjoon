import sys
from collections import Counter


N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

m_list = list(map(int, sys.stdin.readline().split()))

count_list = []

n_counts = Counter(n_list)

for m in m_list:
    count_list.append(n_counts[m])

print(*count_list)