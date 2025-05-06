from collections import deque as dq
h, w = map(int, input().split())
walls = dq(list(map(int, input().split())))

l = walls[0]
ans = 0
mid = max(walls)
while walls:
    r = walls.popleft()
    if r == mid: break
    if l > r:
        ans += (l-r)
    else:
        l = r

if walls: r = walls.pop()
while walls:
    l = walls.pop()
    if r > l:
        ans += (r-l)
    else:
        r = l

print(ans)