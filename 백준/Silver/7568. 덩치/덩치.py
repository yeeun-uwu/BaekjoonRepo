# 키와 몸무게가 모두 커야 함

def label(ppl_list):
    ans = []

    for i in range(n):
        cnt = 1
        for j in range(n):
            if i != j and ppl_list[i][0] < ppl_list[j][0] and ppl_list[i][1] < ppl_list[j][1]:
                cnt += 1
        ans.append(cnt)

    return ans


#입력
n = int(input())
ppl_list = []
for i in range(n):
    x, y = map(int, input().split())
    ppl_list.append((x, y))

print(*label(ppl_list))

#그냥 정렬 과정 없이 더 단순화함. 