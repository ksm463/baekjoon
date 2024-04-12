mat = []

for _ in range(5):
    row = input()
    mat.append(row)

max_len = max(len(row) for row in mat)

result = []
for col in range(max_len):
    for row in range(5):
        if col < len(mat[row]):
            result.append(mat[row][col])

print(''.join(result))