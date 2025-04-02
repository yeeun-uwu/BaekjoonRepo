word_dict = {}

orig_name = input()

for i in orig_name:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
# 문자 갯수 새서 dict로 생성

odd = 0 #홀수 갯수 세기
for i in word_dict.values():
    if i % 2 == 1:
        odd += 1
    if odd >= 2:
        print("I'm Sorry Hansoo")
        quit()
        # 홀수가 2개 이상이면 빠르게 종료

words = dict(sorted(word_dict.items()))
## 사전순으로 정렬
front = []
mid = ""
#앞부분, 중앙 값 변수 생성

for word, nums in words.items():
    for i in range(nums // 2):
        front.append(word)
    if nums % 2 == 1:
        mid = word

#앞부분 생성, 중앙 값 중간에 찾으면 지정

ans = ''.join(front) + mid
front.reverse()
ans += ''.join(front)
print(ans)

##앞뒤 대칭으로 문자열 더해 완료 