def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n 

def lcm(n, m):
    return n * m // gcd(n, m)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))