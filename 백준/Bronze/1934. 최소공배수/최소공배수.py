import sys
import math
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    first, second = map(int, input().split())
    gcd = math.gcd(first, second)
    print((first * second) // gcd)
