import sys

N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

n_set = set(n_list)

M = int(sys.stdin.readline())

m_list = list(map(int, sys.stdin.readline().split()))

bool_list = []

for m in m_list:
    if m in n_set:
        bool_list.append(1)
    else:
        bool_list.append(0)

print(*bool_list)