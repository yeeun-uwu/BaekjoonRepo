def calc(n, piles):
    total = sum(piles)
    avg = total // n
    ans = 0
    dif = 0

    for p in piles:
        dif = p - avg
        if dif > 0:
            ans += dif

    return ans

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

print(calc(n, l))