import sys

input_list = list(sys.stdin.readline().rstrip())

input_list.sort(reverse=True)

print("".join(input_list))
