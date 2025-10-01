# 집이 n개
# 집은 rgb중 하나의 색으로 칠해야 함
# 각각의 색은 비용이 다름 
# 같은 색이 연속으로 오면 안됨
# 최소 비용으로 집을 칠하는 방법

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = cost[0] # 첫집의 각각 rgb비용
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    # 각각 색상에대해 최소값계산 (i번째 집이 어떤색인지에 따라서) 

print(min(dp[n-1]))