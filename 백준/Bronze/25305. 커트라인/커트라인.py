n, k = map(int, input().split())

k_list = list(map(int, input().split()))
k_list.sort(reverse=True)
    
cutline = k_list[k-1]

print(cutline)