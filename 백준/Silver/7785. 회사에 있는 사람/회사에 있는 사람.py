import sys

N = int(sys.stdin.readline())
checkin_list = set()

for _ in range(N):
    name, action = sys.stdin.readline().split()
    
    if action == 'enter':
        checkin_list.add(name)
    elif action == 'leave':
        checkin_list.discard(name)

sorted_checkin_list = sorted(list(checkin_list), reverse=True)

for name in sorted_checkin_list:
    print(name)