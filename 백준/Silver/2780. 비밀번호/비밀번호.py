graph = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8,]
}

def pw_num(n: int):
    dp = [[0] * 10 for _ in range(n+1)]
    #다음 자리 숫자는 연결된 노드 수만큼 가능 

    for digit in range(10):
        dp[1][digit] = 1

    for i in range(2, n+1):
        for current in range(10):
            dp[i][current] = sum(dp[i-1][prev] for prev in graph[current])
            #이전 노드에 연결된 노드들까지..? 만들수 있는 비밀번호의 갯수합
    
    return sum(dp[n]) % 1234567

t = int(input())
for _ in range(t):
    print(pw_num(int(input())))

