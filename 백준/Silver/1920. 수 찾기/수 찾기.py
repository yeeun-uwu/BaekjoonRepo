import sys

def binary_search(arr, target, l, r): #arr 안에서 target 찾기 
    # l, r은 탐색범위 인덱스

    while l<=r:
        mid = (l + r) // 2 

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return 0 
        

'''
    if l > r:
        return 0 
    
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            return binary_search(arr, target, mid+1, r)
        else:
            return binary_search(arr, target, l, mid-1)
'''

input = sys.stdin.read().strip().split("\n")

n = int(input[0]) # 첫줄
arr = list(map(int, input[1].split()))
arr.sort()
m = int(input[2])
targets = list(map(int, input[3].split()))

for t in targets:
    print(binary_search(arr, t, 0, n-1))