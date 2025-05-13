n = int(input())
req = list(map(int, input().split()))
total = int(input())

if total >= sum(req):
    print(max(req))
    exit(0)

def is_possible(m, req:list, total):   
    return sum(min(i, m) for i in req) <= total

def solve(req, total, l, r):
    if l > r:
        return r 
    mid = (l+r) //2 
    if is_possible(mid, req, total):
        return solve(req, total, mid+1, r)
    else: return solve(req, total, l, mid-1)

print(solve(req, total, 0, total))