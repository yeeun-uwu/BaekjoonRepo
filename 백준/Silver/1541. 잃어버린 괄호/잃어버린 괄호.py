
raw = input()

parts_by_minus = raw.split('-') #- 기준으로 나눈 거니까 각각 안쪽만 계산하면 됨

result = sum(map(int, parts_by_minus[0].split('+')))
#빼기 앞 부분은 무조건 더하기된 결과만 존재할테니까 sum 해서 처음 부분 생성

for i in parts_by_minus[1:]: # 첫부분은 이미 계산했음
    result -= sum(map(int, i.split('+')))
    #i는 안에 기호가 있으면 무조건 더하기일테니 sum 하고, 
    # i 자체는 -를 기준으로 나눴기 때문에 빼줌

print(result)