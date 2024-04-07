a = input()

def check(a):
    for i in range(len(a) // 2):
        if a[i] != a[-1-i]:
            return 0
    return 1

print(check(a))