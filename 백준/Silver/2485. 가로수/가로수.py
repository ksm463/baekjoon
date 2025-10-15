import sys
import math
input = sys.stdin.readline

N = int(input())
point_list = []

for _ in range(N):
    L = int(input())
    point_list.append(L)

point_list.sort()
interval_list = []

for i in range(1, N):
    interval_list.append(point_list[i] - point_list[i-1])

g = interval_list[0]

for j in range(1, len(interval_list)):
    g = math.gcd(g, interval_list[j])

total_intervals_needed = (point_list[-1] - point_list[0]) // g
result = total_intervals_needed - (N - 1)
print(result)
