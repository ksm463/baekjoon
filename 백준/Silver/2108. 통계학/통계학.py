import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
nums = []

for _ in range(N):
    i = int(input())
    nums.append(i)

nums.sort()
counts = Counter(nums).most_common()

print(int(sum(nums) / N + 0.5) if sum(nums) >= 0 else int(sum(nums) / N - 0.5))
print(nums[N // 2])
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    print(counts[1][0])
else:
    print(counts[0][0])
print(nums[-1] - nums[0])