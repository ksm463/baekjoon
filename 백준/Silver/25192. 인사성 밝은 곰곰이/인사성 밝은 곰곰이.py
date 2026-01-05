import sys
input = sys.stdin.readline

N = int(input())
con_count = 0
unique_users = set()

for i in range(N):
    text = input().rstrip()
    if text == 'ENTER':
        con_count += len(unique_users)
        unique_users.clear()
    else:
        unique_users.add(text)

con_count += len(unique_users)

print(con_count)