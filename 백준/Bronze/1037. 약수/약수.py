import sys
input = sys.stdin.readline

measure_num = int(input())
measure_list = list(map(int, input().split()))

measure_max = max(measure_list)
measure_min = min(measure_list)

print(measure_max * measure_min)