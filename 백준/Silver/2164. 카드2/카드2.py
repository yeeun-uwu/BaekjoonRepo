from collections import deque

n = int(input())
cards = deque([_ for _ in range(1, n+1)])

while len(cards) != 1:
    cards.popleft()
    first = cards.popleft()
    cards.append(first)

print(*cards)