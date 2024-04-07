a = input().upper()
b = list(set(a))
cnt = []

for i in b:
    count = a.count(i)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(b[(cnt.index(max(cnt)))])

