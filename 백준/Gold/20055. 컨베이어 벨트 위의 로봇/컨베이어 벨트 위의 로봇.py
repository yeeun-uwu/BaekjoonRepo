import sys
from collections import deque

# 입력 받기
n, k = map(int, sys.stdin.readline().strip().split())
dur = list(map(int, sys.stdin.readline().strip().split()))

'''
# 올리는 위치와 내리는 위치
up_pos = 0
down_pos = n - 1  # 올리는 위치에서 (N-1)번째 떨어진 곳이 내리는 위치
'''
steps = 0  # 몇 번째 단계인지
dur_zero = 0  # 내구도가 0인 칸의 개수
robot_pos = [0] * n  # 로봇 위치 (컨베이어 위만 표시)

while dur_zero < k:
    steps += 1  # 단계 증가

    # 1번 과정 > dur과 robot_pos 옮겨 회전
    dur = [dur[-1]] + dur[:-1]
    robot_pos = [robot_pos[-1]] + robot_pos[:-1]
    '''
    up_pos = (up_pos + 1) % (2 * n)
    down_pos = (down_pos + 1) % (2 * n)
    '''

    # 로봇 내리기 (내리는 위치에 로봇이 있다면 제거)
    robot_pos[-1] = 0

    # 2번 과정 시작 > 오른쪽부터 탐색
    for i in range(n - 2, -1, -1):  # 오른쪽에서 왼쪽으로 가면서 탐색. 내리는 위치 제외.
        if robot_pos[i]==1 and robot_pos[i+1]==0 and dur[i+1] >0:
            robot_pos[i+1] = 1
            robot_pos[i] = 0
            dur[i+1] -= 1
            if dur[i+1] == 0:
                dur_zero += 1
        '''
        if robot_pos[i] == 1 and robot_pos[i + 1] == 0: #옆에 로봇 없는지 확인인
            next_pos = (up_pos + i + 1) % (2 * n)  # 로봇이 이동할 내구도 위치
            if dur[next_pos] > 0:
                # 로봇 이동
                robot_pos[i] = 0
                robot_pos[i + 1] = 1 #내리는 위치 제외했어서 인덱스에러 안남남
                dur[next_pos] -= 1
                if dur[next_pos] == 0:
                    dur_zero += 1
                print(f"{next_pos-1} pop!")
                '''

    # 로봇 내리기 (내리는 위치에 로봇이 있다면 제거)
    robot_pos[-1] = 0

    # 3번 과정 시작
    if dur[0] > 0:
        robot_pos[0] = 1
        dur[0] -= 1
        if dur[0] == 0:
            dur_zero += 1
    '''
    if dur[up_pos] > 0 and robot_pos[0] != 1:
        robot_pos[0] = 1  # 올리는 위치에 로봇 추가
        dur[up_pos] -= 1
        #print(f"put {up_pos}")
        if dur[up_pos] == 0:
            dur_zero += 1
            '''
    
    #print(dur)

print(steps)
