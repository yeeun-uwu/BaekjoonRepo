def isPrime(a):
    ans = True
    if a == 1:
        ans = False
        return ans
    for i in range(2, a):
        if a % i == 0:
            ans = False
            break
    return ans

n = int(input())
l = list(map(int, input().split()))

ans = 0
for j in l:
    if isPrime(j):
        ans += 1

print(ans)
