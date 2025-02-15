from itertools import combinations as c

n, m = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
for card in c(cards, 3):
    total = sum(card)
    if best < total <= m:
        best = total
    if best == m:
        break

print(best)