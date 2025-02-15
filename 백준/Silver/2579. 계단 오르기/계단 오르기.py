def calc(t):
    if t == 0:
        return scores[0]  # 첫 번째 계단
    if t == 1:
        return scores[0] + scores[1]  # 두 번째 계단
    if t == 2:
        return max(scores[0] + scores[2], scores[1] + scores[2])  # 세 번째 계단

    if sc[t] != -1:
        return sc[t]  # 이미 계산된 값이 있다면 반환

    # 점화식 적용 (한 칸 전에서 온 경우 vs 두 칸 전에서 온 경우)
    sc[t] = max(calc(t - 2) + scores[t], calc(t - 3) + scores[t - 1] + scores[t])
    return sc[t]

n = int(input()) #계단 갯수
scores = []

for i in range(n):
    scores.append(int(input()))

sc = [-1] * n # 계산 안된 값이 -1, 전체 리스트 미리 생성 
print(calc(n-1))