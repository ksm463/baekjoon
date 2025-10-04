import sys

N = int(sys.stdin.readline())

list_set = []
    
for _ in range(N):
    age_str, name = sys.stdin.readline().split()
    age = int(age_str)
    list_set.append([age, name])

list_set.sort(key = lambda x : x[0])
    
for i in range(N):
    print(list_set[i][0], list_set[i][1])