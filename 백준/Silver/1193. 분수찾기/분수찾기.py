def calc(n):
    num = 0
    cnt = 1
    while(num + cnt < n):
        num += cnt
        cnt += 1
    
    up = n - num
    if cnt % 2 == 0:
        return str(up)+"/"+str(cnt-up+1)
    else:
        return str(cnt-up+1)+"/"+str(up)

x = int(input())
print(calc(x))