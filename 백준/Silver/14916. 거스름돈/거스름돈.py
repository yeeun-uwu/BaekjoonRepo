n = int(input())

ans = 0

if n == 1 or n == 3:
    print(-1)
    exit(0)

while(True):
    if n % 5 == 0:
        ans += n // 5 
        break
    #n이 5의 배수가 되었다면 바로 5로 나눠서 더하고 종료

    n -= 2
    ans += 1
    #n이 5의 배수가 아니라면, n에서 2를 빼고 ans에 2 동전 1개의 갯수를 더함

#사실 n은 5로 나눈 나머지가 0, +-1, +-2인 경우로 나누어지므로 
#반복문도 상당히 짧게 돌아갈듯 
print(ans)