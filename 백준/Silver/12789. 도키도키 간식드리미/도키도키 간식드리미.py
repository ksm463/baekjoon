import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
stack = []
count = 1

for i in num_list:
    stack.append(i)
    
    while stack and stack[-1] == count:
        stack.pop()
        count += 1
        
if not stack:
    print("Nice")
else:
    print("Sad")
