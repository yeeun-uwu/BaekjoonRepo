n = int(input())
scores = list(map(int, input().split()))

final_rank = [0] * n
for i in range(n):
    mid_rank = scores[i] - 1  # 중간 등수도 0~n-1
    final_rank[mid_rank] = i  # i등 기말 = mid_rank번

for r in range(n):  # 중간 등수 기준 출력
    print(r-final_rank[r])
