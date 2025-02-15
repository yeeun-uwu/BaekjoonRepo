n = int(input())
ans = []
for i in range(n):
    ans.append(input())

ans = set(ans) #중복제거
ans = list(ans) # 정렬 쉽게
ans.sort(key = lambda x: (len(x), x))

for i in ans:
    print(i)