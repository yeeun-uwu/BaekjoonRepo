def calc(ans):
    score = 0
    streak = 1

    for i in ans:
        if i == "O":
            score += streak
            streak += 1
        else:
            streak = 1
    
    return score

n = int(input())
for i in range(n):
    ans = list(input())
    print(calc(ans))