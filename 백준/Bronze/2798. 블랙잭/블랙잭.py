from itertools import combinations

cards, lim = map(int, input().split())
card_list = list(map(int, input().split()))

highest_sum = 0

for combo in combinations(card_list, 3):
    present_sum = sum(combo)
    
    if present_sum <= lim and present_sum >= highest_sum:
        highest_sum = present_sum

print(highest_sum)