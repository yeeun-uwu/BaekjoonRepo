

n = int(input())
t = []
p = []
for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi) #입력받음

dp = [0] * (n+1) # 퇴사날까지 리스트로 생성
for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1] # n+1개의 dp 리스트가 있어서 오류 x
    else:
        dp[i] = max(dp[i+1], dp[i+t[i]]+p[i])

print(dp[0])