import sys as s

count = {-1: 0, 0: 0, 1: 0}

def check(x, y, size):
    num = paper[y][x]
    for i in range(y, y+size):
        for j in range(x, x+size):
            if paper[i][j]!=num:
                return False
    return True

def divide(x, y, size):
    if check(x, y, size):
        count[paper[y][x]] += 1
        return
    
    divided = size//3
    for dy in range(3):
        for dx in range(3):
            divide(x+dx*divided, y+dy*divided, divided)

n = int(input())
paper = [list(map(int, s.stdin.readline().strip().split())) for _ in range(n)]

divide(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])