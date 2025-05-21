def maxsum(n: int, arr: list) -> int:
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    return max(dp)

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 출력
print(maxsum(n, arr))