import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
sorted_num_list = sorted(list(set(num_list)))

rank_num = {value : index for index, value in enumerate(sorted_num_list)}

result = []
    
for num in num_list:
    result.append(rank_num[num])

print(*result)
