def calc(h, height_count):
    ans = 0
    for height, count in height_count.items(): 
        if height > h:
            ans += 2 * (height - h) * count
        else:
            ans += (h - height) * count
    return ans


#입력 
n, m, b = map(int, input().split())
ground = []

for i in range(n):
    ground.append(list(map(int, input().split())))

#최소높이 
minh = min(map(min, ground))

#최대높이
s = sum(sum(row) for row in ground)
temp = (s + b) // (n * m)
maxh = min(max(map(max, ground)), temp)
# 지금 설치된 블럭보다 높은 높이로까지 갈필요는없으니까 
height_count = {}
for row in ground:
    for h in row:
        height_count[h] = height_count.get(h, 0) + 1

# calc 함수 최적화
ans_h = 0
ans_t = float('inf')
for i in range(minh, maxh+1):
    temp = calc(i, height_count)

    if temp < ans_t or (temp == ans_t and i > ans_h):
        ans_h = i
        ans_t = temp

print(f"{ans_t} {ans_h}")