from collections import deque as q

k = int(input())
mon = q([])
for i in range(k):
    a = int(input())
    if a == 0:
        mon.pop()
    else:
        mon.append(a)

print(sum(mon))