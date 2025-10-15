# n개의 물건, 각각의 무게 w와 가치 v
# 최대 무게 k 이하로 담을 수 있는 배낭
# 가치의 최댓값
# 배낭 문제 

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)] # i번째 물건까지 j 무게일 때 최대 가치

for i in range(1, n+1):
    w, v = items[i-1]

    for j in range(1, k+1):
        if j < w: # i번째 물건을 못 넣음
            dp[i][j] = dp[i-1][j]
        else: # i번째 물건을 넣을 수 있음
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            # i번째 물건을 넣지 않는 경우, i번째 물건을 넣는 경우
        
print(dp[n][k])