mat = []
max = 0
max_i = 0
max_j = 0

for _ in range(9):
    row = list(map(int, input().split()))
    mat.append(row)

for i in range(9):
    for j in range(9):
        if mat[i][j] >= max:
            max = mat[i][j]
            max_i = i+1
            max_j = j+1

print(max)
print(max_i, max_j)