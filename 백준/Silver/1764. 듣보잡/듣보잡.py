import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_set = set()

for i in range(N):
    n_set.add(input().strip())

m_set = set()

for i in range(M):
    m_set.add(input().strip())

nm_list = sorted(list(n_set & m_set))

print(len(nm_list))
for k in nm_list:
    print(k)