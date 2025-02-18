def number(n): #n번째 종말의 수를 찾는 함수
    cnt = 0
    num = 666

    while True:
        if '666' in str(num):
            cnt +=1
            if cnt == n:
                break
        num += 1
    
    return num

n = int(input())
print(number(n))