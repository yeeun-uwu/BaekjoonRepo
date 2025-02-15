from math import *
n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())
ans_t = 0

for s in sizes:
    ans_t += ceil(s/t)

print(ans_t)
print(n//p, n%p)