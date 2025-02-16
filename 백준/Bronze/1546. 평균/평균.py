n = int(input())
scores = list(map(int, input().split()))
high_score = max(scores)
average = (sum(scores) / n) / high_score * 100
print(average)