def count_changes(start_color, x, y):
        changes = 0
        for i in range(8):
            for j in range(8):
                expected_color = (start_color + i + j) % 2  
                # 체스판에서 칸의 색은 (i+j) % 2
                if board[x + i][y + j] != expected_color:
                    changes += 1
        return changes

def min_changes_to_chessboard(board, M, N):
    
    # 모든 8x8 부분에 대해 계산
    min_changes = 64 
    
    for i in range(M - 7):  # 8x8의 첫번째 칸을 (i, j)로 시작
        for j in range(N - 7):
            # 왼쪽 위가 흰색(0)인 경우와 검은색(1)인 경우의 변화를 각각 계산
            changes_white_first = count_changes(0, i, j)
            changes_black_first = count_changes(1, i, j)
            
            # 그 중 더 적은 변경 횟수를 선택
            min_changes = min(min_changes, changes_white_first, changes_black_first)
    
    return min_changes


# 입력 받기
m, n = map(int, input().split())
board = [list(input().strip()) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == "B":
            board[i][j] = 1
        else:
            board[i][j] = 0

result = min_changes_to_chessboard(board, m, n)
print(result)
