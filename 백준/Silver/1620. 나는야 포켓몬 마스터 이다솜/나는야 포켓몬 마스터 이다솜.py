import sys

input = sys.stdin.readline

N, M = map(int, input().split())
index_dict = {}

for i in range(1, N+1):
    pokemon_name = input().rstrip()
    index_dict[i] = pokemon_name
    index_dict[pokemon_name] = i
    
for i in range(M):
    name_or_index = input().rstrip()
    if name_or_index.isdigit():
        print(index_dict[int(name_or_index)])
    else:
        print(index_dict[name_or_index])
