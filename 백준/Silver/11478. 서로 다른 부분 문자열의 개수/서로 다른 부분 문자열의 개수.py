import sys
input = sys.stdin.readline

S = input().strip()
len_s = len(S)
unique_substrings = set()

for i in range(len_s):
    for j in range(i, len_s):
        unique_substrings.add(S[i:j+1])

print(len(unique_substrings))
