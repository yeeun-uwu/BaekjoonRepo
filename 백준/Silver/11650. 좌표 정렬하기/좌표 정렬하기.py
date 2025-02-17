n = int(input())
pos = []

for i in range(n):
    x,y = map(int, input().split())
    pos.append([x, y])

pos.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    print(*pos[i])