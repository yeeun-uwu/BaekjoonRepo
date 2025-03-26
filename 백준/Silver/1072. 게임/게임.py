import math 

x, y = map(int, input().split())
init_z = math.trunc((y * 100/ x))
#print(init_z)

target_z = init_z + 1

left, right = 0, 10**9  # x범위만큼 탐색색

# 이분탐색
while left < right:
    mid = (left + right) // 2
    new_z = math.trunc(((y + mid) * 100/ (x + mid)) )

    if new_z >= target_z:
        right = mid  # 더 적은 게임 횟수로 목표 승률을 달성할 수 있다면 범위를 좁힘
    else:
        left = mid + 1  # 목표 승률에 도달하지 못했다면 게임 횟수를 늘려야 함

if  math.trunc(((y + left) * 100 / (x + left))) >= target_z:
    print(left)
else:
    print(-1)