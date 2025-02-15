n = int(input())
l = list(map(int, input().split()))  # 수열 생성

dp = [1] * n

for i in range(n):
    for j in range(i):
        if l[j] < l[i]: # 증가하는지
            dp[i] = max(dp[i], dp[j]+1) #원래의 dp[i] 값과 
            #dp[j](j번째를 마지막으로 하는 증가수열) + 1 (지금 값이 대해졋으므로)를 비교해서 저장

print(max(dp))