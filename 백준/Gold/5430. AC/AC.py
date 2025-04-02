#r: 순서 뒤집기
#d: 첫 수 버리기 > 비어있으면 에러
import sys
from collections import deque

# 빠른 입출력

t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

result = []

for _ in range(t):
    func = list(sys.stdin.readline().strip())  # 명령어
    l_n = int(sys.stdin.readline().strip())  # 숫자 개수
    num_str = sys.stdin.readline().strip()  # 숫자 리스트
    num_str = num_str.strip("[]")


    # 숫자 리스트 처리
    if num_str:
        nums = deque(map(int, num_str.split(",")))
    else:
        nums = deque()

    reverse_flag = False
    error_flag = False

    for cmd in func:
        
        if cmd == "R":
            reverse_flag = not reverse_flag  # 뒤집기 플래그 전환
        elif cmd == "D":
            if not nums:
                result.append("error\n")
                error_flag = True # 에러 출력했다는거 전달해야댐 
                break
            if reverse_flag:
                nums.pop()  # 뒤에서 제거
            else:
                nums.popleft()  # 앞에서 제거

    if not error_flag:
        if reverse_flag:
            nums.reverse()  # 최종적으로 한 번만 뒤집기
        result.append(f"[{','.join(map(str, nums))}]\n")

# 최종 결과를 한 번에 출력
print("".join(result))
