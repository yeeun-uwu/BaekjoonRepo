import sys as s

def avg(numbers):
    return round(sum(numbers) / len(numbers))

def mid(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) // 2]

def most(nums):
    sorted_items = sorted(nums.items(), key=lambda x: (-x[1], x[0]))  # 빈도 내림차순, 값 오름차순 정렬
    if len(sorted_items) > 1 and sorted_items[0][1] == sorted_items[1][1]:  
        return sorted_items[1][0]  # 최빈값이 여러 개일 경우 두 번째로 작은 값 반환
    return sorted_items[0][0]

def ranges(nums):
    sorted_keys = sorted(nums.keys())  #딕셔너리 키만 쓰므로 키 정렬
    return sorted_keys[-1] - sorted_keys[0]  # 최댓값 - 최솟값

n = int(s.stdin.readline().strip())
numbers = [int(s.stdin.readline().strip()) for _ in range(n)]

nums = {}
for i in numbers:
    nums[i] = nums.get(i, 0) + 1  # 딕셔너리 get()을 사용하여 간결화

print(avg(numbers))
print(mid(numbers))
print(most(nums))
print(ranges(nums))
