# n개의 줄이 주어졌을 때
n = int(input())

#인접 행렬 입력받음
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

adj_matrix_res = adj_matrix # 결과를 저장할 행렬 초기화

# 모든 정점에 대해서 경로 찾기
for k in range(n):
    #i에서 j로 가는 경로가 존재하는지 확인하는 걸 여러번 반복해서 중간 경유지 거쳐서 도착 가능한지 확인
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][k] and adj_matrix[k][j]:  # i에서 k로 가는 경로가 있고, k에서 j로 가는 경로가 있다면
                adj_matrix_res[i][j] = 1  # i에서 j로 가는 경로가 있다고 표시

# 결과 행렬 출력
for row in adj_matrix_res:
    print(' '.join(map(str, row)))
