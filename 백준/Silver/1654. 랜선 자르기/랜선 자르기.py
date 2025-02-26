import sys as s

def can_make(lines, len, n):
    if n == 0 or len == 0:
        return True
    ans = 0
    for i in lines:
        ans += i // len

    return True if n <= ans else False

def max_length(lines, n):
    left, right = 0, sum(lines)//n
    result = 0
    #이분탐색 이용, 오른쪽 끝은 최대길이로 시작 (전체길이를 n보다 나눈것보다는 짧아야겠지지)
    while left <= right:
        mid = (left+right) // 2
        if can_make(lines, mid, n):
             result = mid #가능하다면 일단 저장하고 더 긴 길이 시도
             left = mid + 1
        else:
            right = mid - 1 #안되면 짧게

    return result


k, n = map(int, input().split())
lines = [int(s.stdin.readline().strip()) for _ in range(k)]
print(max_length(lines, n))