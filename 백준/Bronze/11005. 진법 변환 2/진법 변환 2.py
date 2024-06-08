a, b = map(int, input().split())

def div_n(a, b):
    c = ''
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while a > 0:
        a, d = divmod(a, b)
        c += alphabet[d]
    
    return c[::-1]

print(div_n(a, b))