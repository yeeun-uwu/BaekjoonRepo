from collections import deque as dq

gears = [dq(map(int, input().strip())) for _ in range(4)]
#기어 상태 입력

k = int(input())
#회전 횟수 입력
rot = [tuple(map(int, input().split())) for _ in range(k)]
#회전 명령 입력

def rotate(gear, direction):
    checked = [False] * 4 #회전 여부 확인했는지
    rotate_dir = [0] * 4 #회전 방향
    rotate_dir[gear] = direction #초기 기어 방향 설정
    checked[gear] = True #초기 기어 확인함

    #왼쪽 기어 회전
    for i in range(gear - 1, -1, -1):
        if gears[i + 1][6] != gears[i][2]: #맞닿은 극이 다르면
            rotate_dir[i] = -rotate_dir[i + 1] #반대 방향으로 회전
            checked[i] = True #확인함
        else:
            break #극이 같으면 회전 안함
    
    #오른쪽 기어 회전
    for i in range(gear + 1, 4):
        if gears[i - 1][2] != gears[i][6]: #맞닿은 극이 다르면
            rotate_dir[i] = -rotate_dir[i - 1] #반대 방향으로 회전
            checked[i] = True #확인함
        else:
            break #극이 같으면 회전 안함

    #회전
    for i in range(4):
        if checked[i]: #확인한 기어만 회전
            if rotate_dir[i] == 1: #시계 방향
                gears[i].appendleft(gears[i].pop())
            elif rotate_dir[i] == -1: #반시계 방향
                gears[i].append(gears[i].popleft())

for gear, direction in rot:
    rotate(gear - 1, direction) #기어 번호를 조정하고 회전 명령 실행

#기어 점수 계산
score = 0
for i in range(4):
    if gears[i][0] == 1: #첫 번째 톱니가 N극이면
        score += 2 ** i #점수 계산

print(score) #최종 점수 출력