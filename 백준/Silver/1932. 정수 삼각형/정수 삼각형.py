# 정수 삼각형의 크기와 정수 삼각형 주어짐
# 맨 위층에서부터 시작하여 아래층으로 내려올 때,
# 바로 아래 (왼, 오) 중 한 수를 더함
# 가장 큰 합을 구하는 프로그램 작성

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

def solution(triangle):
    dp = triangle[:]  # dp 테이블 초기화 (더하기 편하게 삼각형 배열 그대로)
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:  # 맨 왼쪽일 경우 
                dp[i][j] += dp[i - 1][j]
            elif j == i:  # 맨 오른쪽일 경우
                dp[i][j] += dp[i - 1][j - 1]
            else:  # 중간 경우들 
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])  # 마지막 행에서 최대값 반환

print(solution(triangle))
