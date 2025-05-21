#1로 시작, 11을 부분 문자열 x 
#dp[n][0] = dp[n-1][0] + dp[n-1][1]
#dp[n][1] = dp[n-1][0]

n = int(input())

dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i - 1][0]

print(dp[n][0] + dp[n][1])