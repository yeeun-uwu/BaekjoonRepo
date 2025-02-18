#5를 가장 많이 넣는 경우부터 역으로 계산
def calc(n):
    ans = 0
    num5 = 0
    num3 = -1

    for i in range(n//5, -1, -1):
        num = n - (i * 5)
        if num % 3 == 0:
            num5 = i
            num3 = num//3
            break
    
    ans = num5 + num3

    return ans

n = int(input())
print(calc(n))