# 높이 h 이상의 나무는 다 그 높이에서 잘린다

n, m = map(int, input().split())
trees = list(map(int, input().split()))
if sum(trees) == m:
    print(0)
    exit()

def cut_tree(trees, height):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

# 이진탐색으로 최적화해야될듯

def binary_search():
    start, end = 0, max(trees)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = cut_tree(trees, mid)
        if total < m:  # 나무가 부족한 경우
            end = mid - 1
        else:  # 나무가 충분한 경우
            result = mid  # 일단 결과 저장
            start = mid + 1  # 더 높은 높이에서 잘라보기
    return result

print(binary_search())
