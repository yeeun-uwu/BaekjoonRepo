m = int(input())

def count_z(n: int, m):   
    cnt = 0
    while n > 0:
        n //= 5
        cnt += n
    return cnt

def solve(m):
    l, r = 0, 5*m
    res = -1

    while l<=r:
        mid = (l+r)//2
        i = count_z(mid, m)
        if i == m:
            res = mid
            r = mid - 1
        elif i > m:
            r = mid-1
        else:
            l = mid+1
    return res

print(solve(m))