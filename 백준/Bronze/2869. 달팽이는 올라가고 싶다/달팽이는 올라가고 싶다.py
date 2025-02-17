from math import ceil as c

def days(n, m, h):
    if n>=h:
        return 1

    return c(((h-n) / (n-m))) + 1
#하루에 n-m을 올라가고, 마지막 날은 안미끄러지니까 n을 올라가서 h-n을 n-m으로 나누고 하루 추가가

a, b, v = map(int, input().split())
print(days(a, b, v))