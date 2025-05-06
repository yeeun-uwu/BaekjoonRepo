def ans(current):
    global answer
    if current > n:
        return
    if current > answer:
        answer = current
    for a in k:
        ans(current*10+a)

n, nums = map(int, input().split())
k = list(map(int, input().split()))
answer = 0
ans(0)
print(answer)