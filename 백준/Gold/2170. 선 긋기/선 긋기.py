import sys as s 

n = int(input())
lines = [tuple(map(int, s.stdin.readline().strip().split())) for _ in range(n)]
lines.sort()

t = 0
l, r = lines[0]

for f, e in lines[1:]:
    if f <= r: #겹치면
        r = max(r, e)
        l = min(l, f)
    else:
        t += r - l
        l, r = f, e

t += r - l
print(t)