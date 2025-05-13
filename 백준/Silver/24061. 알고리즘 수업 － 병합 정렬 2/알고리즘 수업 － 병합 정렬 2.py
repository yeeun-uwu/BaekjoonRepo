import sys as s 
n, k = map(int, input().split())
a = list(map(int, input().split()))

def merge(a: list, p: int, q: int, r: int):
    global cnt, rst
    tmp = []
    i, j = p, q+1

    while i<=q and j<=r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    while i <= q:
        tmp.append(a[i])
        i += 1
    
    while j <= r:
        tmp.append(a[j])
        j += 1

    for _ in range(len(tmp)):
        a[p+_] = tmp[_]
        cnt +=1 
        if cnt == k:
            rst = a[:]


def merge_sort(a: list, p: int, r: int):
    if p < r:
        q = (p+r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

cnt = 0
rst = []

merge_sort(a, 0, n-1)
if rst:
    print(*rst)
else:
    print(-1)