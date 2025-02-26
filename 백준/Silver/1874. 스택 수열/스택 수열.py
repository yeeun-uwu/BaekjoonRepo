def calcs(n, target):
    stack = []
    result = []
    cnt = 1
    idx = 0  # target 리스트 접근

    while idx < n:
        # 스택의 top이 target[idx]와 같다면 pop
        if stack and stack[-1] == target[idx]:
            stack.pop()
            result.append("-")
            idx += 1  # target의 다음 요소 확인
        # cnt를 push할 수 있다면 push
        elif cnt <= n:
            stack.append(cnt)
            result.append("+")
            cnt += 1
        # 더 이상 push할 수도 없고 pop도 안 되는 경우
        else:
            return ["NO"]
    
    return result


n = int(input())
target = [int(input()) for _ in range(n)]
for i in calcs(n, target):
    print(i)